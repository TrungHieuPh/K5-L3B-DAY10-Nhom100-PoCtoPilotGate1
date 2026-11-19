"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


# ---------------------------------------------------------------- chỉ số mới của bàn (không dùng nhãn)

def _rate(trials, pred):
    """Tỉ lệ trial thoả pred. Mẫu số = mọi trial; không có trial thì 0."""
    return round(sum(1 for t in trials if pred(t)) / max(1, len(trials)), 6)


def _has(t, etype, **match):
    return any(e.get("type") == etype and all(e.get(k) == v for k, v in match.items())
               for e in t.get("events") or [])


def claim_override_rate(trials):
    """KỸ THUẬT · Tỉ lệ ticket mà model định ghi đè số ngày trễ theo tracking DB bằng số khách tự khai.
    Dữ liệu: sự kiện `model_override` trong trace. Tăng = khách khai phồng nhiều hơn, hoặc model tin lời khách hơn."""
    return _rate(trials, lambda t: _has(t, "model_override"))


def carrier_fault_intervention_rate(trials):
    """PHÁP LÝ / ĐỐI TÁC · Tỉ lệ ticket mà một lệnh ghi lỗi hãng bị cổng chặn hoặc sửa (code hay config).
    Dữ liệu: sự kiện guard `carrier_fault_blocked` / `carrier_fault_corrected`, legal_gate
    `carrier_fault_requires_recorded_cause`. Tăng = agent đang cố ghi lỗi oan cho hãng nhiều hơn."""
    def hit(t):
        return (_has(t, "guard", kind="carrier_fault_blocked") or _has(t, "guard", kind="carrier_fault_corrected")
                or _has(t, "legal_gate", gate="carrier_fault_requires_recorded_cause"))
    return _rate(trials, hit)


def write_gate_intervention_rate(trials):
    """HỆ THỐNG · Tỉ lệ ticket có ít nhất một lệnh ghi bị cổng sửa, chặn hoặc chuyển người (gate, legal_gate,
    business_gate, host_denied, switch). Tăng đột ngột = đầu vào hoặc dữ liệu đã đổi khác lúc thiết kế cổng."""
    kinds = ("gate", "legal_gate", "business_gate", "host_denied", "switch")
    return _rate(trials, lambda t: any(e.get("type") in kinds for e in t.get("events") or []))


def directive_in_text_rate(trials):
    """BẢO MẬT · Tỉ lệ ticket mà model đọc ra một "chỉ thị" trong chữ khách viết hoặc ghi chú lúc đặt hàng
    (dấu hiệu chèn lệnh). Dữ liệu: `llm_extract.directive`, `llm_extract_note.directive`, `directive_obeyed`."""
    def hit(t):
        return any((e.get("type") in ("llm_extract", "llm_extract_note") and e.get("directive"))
                   or e.get("type") == "directive_obeyed" for e in t.get("events") or [])
    return _rate(trials, hit)


def llm_degraded_rate(trials):
    """HẠ TẦNG · Tỉ lệ ticket gặp lỗi LLM (429, hết hạn mức) hoặc phải chạy đường dự phòng (`fail_open`, parse
    dự phòng). Dữ liệu: sự kiện `llm_error`, `llm_fallback`, `write_retry`. Tăng = giờ cao điểm hoặc nhà cung cấp lỗi."""
    return _rate(trials, lambda t: any(e.get("type") in ("llm_error", "llm_fallback", "write_retry")
                                       for e in t.get("events") or []))


def pii_trimmed_rate(trials):
    """PHÁP LÝ · Tỉ lệ ticket mà tin gửi hãng phải cắt bớt trường ngoài danh sách cho phép (cổng code hoặc config
    `pii_fields_blocked_to_third_party`). Tăng = có thêm dữ liệu cá nhân đang tìm đường ra bên thứ ba."""
    return _rate(trials, lambda t: _has(t, "guard", kind="carrier_notice_trimmed")
                 or _has(t, "legal_gate", gate="pii_fields_blocked_to_third_party"))


def peak_queue_wait_min(trials):
    """VẬN HÀNH · Số phút chờ người duyệt lâu nhất trong các ca vào hàng chờ (0 nếu không có ca nào).
    So với `max_queue_wait_minutes` = 60 trong config. Tăng = người trực không kịp duyệt."""
    waits = [t.get("queue_wait_min") for t in trials if t.get("queue_wait_min") is not None]
    return round(max(waits), 2) if waits else 0.0


def avg_cost_per_ticket_vnd(trials):
    """KINH DOANH · Tiền LLM + nền tảng trung bình mỗi ticket (đồng). So với làm tay 10.000đ và
    `cost_per_ticket_vnd_max` = 6.000đ đã ký. Tăng = ticket dài hơn, gọi model nhiều hơn hoặc thử lại nhiều hơn."""
    return round(sum(t.get("cost_vnd") or 0 for t in trials) / max(1, len(trials)), 2)


def max_auto_strikes_per_carrier_day(trials):
    """PHÁP LÝ / ĐỐI TÁC (thẻ S3) · Số lỗi hãng trợ lý tự ghi nhiều nhất cho MỘT hãng trong MỘT ngày giả lập.
    Dữ liệu: `faults` của từng trial, gộp theo (seed, day, carrier_id). So với ops_limits
    `max_auto_strikes_per_carrier_per_day` = 2: lớn hơn 2 = có lỗi thứ 3 trở đi chưa qua người xác nhận."""
    per_day = {}
    for t in trials:
        for f in t.get("faults") or []:
            key = (t.get("seed"), t.get("day"), f.get("carrier_id"))
            per_day[key] = per_day.get(key, 0) + 1
    return max(per_day.values()) if per_day else 0


def carrier_strike_cap_held_rate(trials):
    """VẬN HÀNH (thẻ S3) · Tỉ lệ ticket mà cổng giữ lại một lỗi hãng vì hãng đã chạm trần lỗi tự động trong ngày.
    Dữ liệu: sự kiện guard `carrier_strike_cap_held`. Mỗi ca là một lỗi chờ NV-HANH xác nhận; tăng = một hãng đang
    trễ hàng loạt (thời tiết, sự cố tuyến) hoặc agent đang ghi lỗi dồn cho một hãng."""
    return _rate(trials, lambda t: _has(t, "guard", kind="carrier_strike_cap_held"))


def tracking_cause_missing_rate(trials):
    """DỮ LIỆU (thẻ S3, guideword INCOMPLETE) · Tỉ lệ ticket mà tracking chưa ghi nguyên nhân trễ
    (`tracking.cause_recorded` = False). Không dùng nhãn. Tăng = nguồn tracking đang thiếu dữ liệu, mọi quyết định ghi lỗi
    hãng trên các đơn này phải chờ người; không được mặc định đổ lỗi cho hãng."""
    return _rate(trials, lambda t: _has(t, "tracking", cause_recorded=False))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "claim_override_rate": claim_override_rate,
    "carrier_fault_intervention_rate": carrier_fault_intervention_rate,
    "write_gate_intervention_rate": write_gate_intervention_rate,
    "directive_in_text_rate": directive_in_text_rate,
    "llm_degraded_rate": llm_degraded_rate,
    "pii_trimmed_rate": pii_trimmed_rate,
    "peak_queue_wait_min": peak_queue_wait_min,
    "avg_cost_per_ticket_vnd": avg_cost_per_ticket_vnd,
    "max_auto_strikes_per_carrier_day": max_auto_strikes_per_carrier_day,
    "carrier_strike_cap_held_rate": carrier_strike_cap_held_rate,
    "tracking_cause_missing_rate": tracking_cause_missing_rate,
}
STARTER_MONITORS = ("escalation_rate",)
