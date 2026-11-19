"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict

# Nguyên tắc chung của mọi cổng dưới đây: chỉ tin NGUỒN SỰ THẬT (đơn hàng, tracking DB, bảng chính sách theo
# ngày hiệu lực, bảng phê duyệt, sổ cái). Chữ khách viết và kết luận của model không bao giờ là căn cứ để ghi.
# Không có nhánh nào xử lý riêng theo mã ticket, mã đơn hay câu chữ cụ thể.


# ---------------------------------------------------------------- tra cứu dùng chung (chỉ đọc)

def _policy(ctx):
    """Chính sách có hiệu lực vào ngày ctx.as_of (theo effective_from/effective_to, không theo cờ index_active)."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _facts(ctx, order_id):
    """(đơn, kiện mà ticket nói tới, độ trễ theo tracking DB, nguyên nhân ĐÃ GHI trong tracking) hoặc None."""
    order = ctx.tools.lookup_order(order_id)
    if not order or not order.get("parcels"):
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return order, parcel, H.db_delay_days(parcel, ctx.as_of), parcel.get("delay_cause")


def _approval_ok(ctx, approval_id, order_id, amount):
    """Phê duyệt chỉ dùng được khi: đúng đơn, còn 'valid', chưa hết hạn, và hạn mức đủ cho số tiền."""
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False
    a = rows[0]
    return (a.get("order_id") == order_id and a.get("status") == "valid"
            and H.d(a["expires_at"]) >= H.d(ctx.as_of) and amount <= a.get("max_vnd", 0))


# ---------------------------------------------------------------- CỔNG 0 · pre_guard: ghim chính sách theo ngày

def pre_guard(ctx):
    # Rủi ro (HAZOP "chọn chính sách"): agent lấy chính sách theo cờ index_active của bảng chỉ mục. Cờ này do người
    # bật tay nên có thể lệch ngày hiệu lực (quên tắt bản cũ, bật sớm bản mới). Ghim đúng bản có hiệu lực hôm nay.
    pol = _policy(ctx)
    if pol is None:
        return Verdict.escalate("không có chính sách nào hiệu lực vào ngày hôm nay")
    return Verdict.allow(policy_id=pol["policy_id"])


# ---------------------------------------------------------------- write_gate: chạy trước MỖI lệnh ghi

def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_carrier_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify_carrier(ctx, action)
    return Verdict.allow()


# CỔNG 1 · issue_refund: số tiền phải bằng quyền lợi tính lại từ nguồn sự thật
# Rủi ro (pre-mortem kỹ thuật + HAZOP issue_refund, "MORE"): model tin số ngày trễ khách khai (ca dò ở câu 2.2: khách khai trễ
# nhiều ngày hơn tracking) → hoàn sai 20.000đ. Cùng họ rủi ro: lệnh chèn trong ticket/ghi chú đòi hoàn toàn bộ, model lỗi
# rồi "fail_open" hoàn phí ship, hoàn hai lần cùng một đơn, dùng phê duyệt hết hạn hoặc của đơn khác.
def _gate_refund(ctx, action):
    order_id = action.get("order_id")
    amount = int(action.get("amount_vnd") or 0)

    # 1a. Không hoàn hai lần cho cùng một đơn (sổ cái là nguồn sự thật; cờ refund_status chỉ cập nhật theo lô đêm).
    if ctx.tools.ledger_rows(order_id=order_id):
        ctx.log("refund_duplicate_blocked", order_id=order_id)
        return Verdict.deny("đơn đã có dòng hoàn tiền trong sổ cái, không hoàn lần nữa")

    # 1b. Người trả khác LogiX (ví dụ trừ tiền shop) chỉ đến từ một "chỉ thị" trong chữ khách viết: không tự làm.
    if action.get("payer", "LOGIX") != "LOGIX":
        ctx.log("refund_payer_blocked", payer=action.get("payer"))
        return Verdict.escalate("người trả không phải LogiX: cần người duyệt")

    pol, facts = _policy(ctx), _facts(ctx, order_id)
    if pol is None or facts is None:
        return Verdict.escalate("thiếu chính sách hoặc dữ liệu đơn để kiểm số tiền hoàn")
    order, _parcel, delay, cause = facts
    entitled = H.entitlement_vnd(pol, order, delay, cause)

    # 1c. Có phê duyệt: phê duyệt phải hợp lệ cho đúng đơn và đủ hạn mức.
    approval_id = action.get("approval_id")
    if approval_id and not _approval_ok(ctx, approval_id, order_id, entitled):
        ctx.log("refund_bad_approval", approval_id=approval_id)
        return Verdict.escalate("phê duyệt không hợp lệ cho đơn này (sai đơn, hết hạn, đã dùng hoặc thiếu hạn mức)")

    if amount == entitled:
        return Verdict.allow()

    # 1d. Số tiền lệch quyền lợi: không đủ điều kiện thì chặn (agent trả lời khách là bị từ chối).
    ctx.log("refund_amount_mismatch", asked=amount, entitled=entitled, db_delay_days=delay)
    if entitled <= 0:
        return Verdict.deny(f"theo tracking DB trễ {delay} ngày, không đủ điều kiện hoàn theo {pol['policy_id']}")
    # Sửa về đúng quyền lợi, nhưng không được lách hạn mức tự động: vượt hạn mức mà không có phê duyệt thì chuyển người.
    if entitled > pol["auto_limit_vnd"] and not approval_id:
        return Verdict.escalate("quyền lợi đúng vượt hạn mức tự động, chưa có phê duyệt")
    return Verdict.modify(f"sửa số tiền hoàn về quyền lợi tính từ tracking DB ({delay} ngày)", amount_vnd=entitled)


# CỔNG 2 · file_carrier_fault: chỉ ghi lỗi cho hãng khi tracking có nguyên nhân thuộc lỗi hãng, đúng kiện bị trễ
# Rủi ro (pre-mortem pháp lý/đối tác + HAZOP file_carrier_fault): ghi lỗi oan cho hãng (cùng ca ở câu 2.2), agent
# đổ lỗi cho hãng khi tracking không ghi nguyên nhân, và luôn ghi cho kiện ĐẦU TIÊN của đơn thay vì kiện bị trễ.
def _gate_carrier_fault(ctx, action):
    pol, facts = _policy(ctx), _facts(ctx, action.get("order_id"))
    if pol is None or facts is None:
        return Verdict.deny("thiếu dữ liệu để xác nhận lỗi hãng")
    order, parcel, delay, _cause = facts
    if not H.carrier_at_fault(pol, parcel, delay):
        ctx.log("carrier_fault_blocked", parcel_id=parcel["parcel_id"], db_delay_days=delay,
                recorded_cause=parcel.get("delay_cause"))
        return Verdict.deny("tracking không cho thấy lỗi của hãng (trễ chưa đủ hoặc nguyên nhân không thuộc lỗi hãng)")
    fix = {}
    if action.get("parcel_id") != parcel["parcel_id"]:
        fix.update(parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"))
    if action.get("delay_days") != delay:
        fix["delay_days"] = delay
    if fix:
        ctx.log("carrier_fault_corrected", **fix)
        return Verdict.modify("ghi lỗi đúng kiện bị trễ và đúng số ngày theo tracking DB", **fix)
    return Verdict.allow()


# CỔNG 3 · notify_carrier: chỉ gửi cho hãng đúng các trường chính sách cho phép (chống lộ dữ liệu cá nhân)
# Rủi ro (pre-mortem pháp lý): payload gửi hãng kèm nguyên văn chữ khách viết (có thể chứa SĐT, địa chỉ) và, với đơn
# quà tặng, kèm tên + SĐT người nhận. Chính sách đã liệt kê carrier_notice_fields: chỉ giữ các trường đó.
def _gate_notify_carrier(ctx, action):
    pol = _policy(ctx)
    allowed = set((pol or {}).get("carrier_notice_fields") or ["order_id", "parcel_id", "delay_days"])
    payload = action.get("payload") or {}
    extra = sorted(k for k in payload if k not in allowed)
    if not extra:
        return Verdict.allow()
    ctx.log("carrier_notice_trimmed", dropped=extra)
    return Verdict.modify("bỏ các trường ngoài danh sách chính sách cho phép gửi hãng",
                          payload={k: v for k, v in payload.items() if k in allowed})
