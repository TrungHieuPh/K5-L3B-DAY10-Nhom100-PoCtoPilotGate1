# Phiếu B · Đo, rủi ro, cổng vòng 1 và quyết định v1 · Khối 2A + 2B + chốt (phút 65–115)

**Bàn:** ______

Tiêu chí đã ký ở Phiếu A. Từ phút 65 bàn mới được chạy trợ lý. Khối 2A (65–85) chưa sửa code hay config. Khối 2B (85–105) sửa
`lab10/guards.py` và `config/operating_gates.json`. Phút 105–115 chốt cổng vòng 1 rồi viết quyết định v1. Sau phút 115 không sửa phiếu này
(trừ khi Phiếu C bảo "mở lại" một ô và ghi bằng bút khác màu).

**Mục lục**
- [B0 · Nhật ký lần chạy vòng 1 (suốt khối)](#b0)
- [B1 · Câu 2.1 · Lần chạy đầu tiên, cổng tự chặn hay người duyệt · phút 65–71](#b1)
- [B2 · Câu 2.2 · Bảng soát lỗi `T-002@55` · phút 71–75](#b2)
- [B3 · Câu 2.3 · Bản đồ dữ liệu và ví dụ drift · phút 65–75](#b3)
- [B4 · Câu 2.4 · HAZOP vòng 1 · phút 65–75](#b4)
- [B5 · Câu 2.4 · Checklist 9 nhóm việc, lần 1 · phút 70–75](#b5)
- [B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa · phút 75–85](#b6)
- [B7 · Câu 2.6–2.10 · Cổng phòng ngừa, runbook phần 1–3, giờ cao điểm · phút 85–105](#b7)
- [B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 · phút 105–115](#b8)

---

<a id="b0"></a>

## B0 · Nhật ký lần chạy vòng 1

*Yêu cầu: ít nhất 3 lần chạy, mỗi lần đổi một thứ, có mã lần chạy và khoảng tin cậy.* Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi
một dòng vào `runs/journal.jsonl`. Việc của bàn là điền cột "Đổi MỘT thứ gì" (tham số `--note`) và cột "Kết luận".
Mọi con số trong quyết định Gate 1 phải trỏ về một dòng ở đây hoặc ở Phiếu C mục C0.

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | base · base | (baseline, chưa có cổng) | | | | | |
| 2 | | base · after | (cổng vòng 1, thử trước khi chốt) | | | | | |
| 3 | | base · prepared | (cổng vòng 1 đã chốt) | | | | | |
| 4 | | | | | | | | |

---

<a id="b1"></a>

## B1 · Câu 2.1 · Lần chạy đánh giá đầu tiên

```bash
python3 -m lab10.eval --suite base --stage base --note "baseline"
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

- Mã lần chạy: `__________` (ghi cả vào B0 dòng 1)
- Ngưỡng đã ký nào `[CHƯA]` đạt: …
- Khối "kinh doanh và vận hành" ở cuối output: dòng nào đáng lo? …
- Khối "theo kho và hãng": kho hoặc hãng nào có số xấu nhất? …

**Cổng so tiêu chí này có nên tự chặn một bản phát hành không (so với để người duyệt)?**

| Lý lẽ ủng hộ tự chặn | Lý lẽ phản đối |
|---|---|
| | |

Khuyến nghị (khoanh một): **tự chặn · người duyệt · kết hợp**. Vì: …

---

<a id="b2"></a>

## B2 · Câu 2.2 · Bảng soát lỗi cho `T-002@55`

```bash
python3 -m lab10.trace --suite base --ticket T-002 --seed 55
```

**Cách làm, giữ nguyên ba phần:** (1) ghi lại từng lỗi bằng **cái người ta thực sự thấy**, ai gặp, mức hệ trọng,
và xếp vào một trong ba **loại lỗi**; (2) đưa lỗi qua bộ câu hỏi để tìm **nguồn**; (3) viết **hướng xử lý**: vì sao người ta coi
đó là lỗi, người ta đi tiếp bằng đường nào, hệ thống học được gì.

Ba loại lỗi:
- **Giới hạn của hệ thống**: hệ thống không thể trả lời đúng, hoặc không trả lời được, vì giới hạn vốn có.
- **Lỗi ngữ cảnh**: hệ thống "chạy đúng thiết kế" nhưng người dùng thấy sai, vì hành động không được giải thích, trái với hình dung của họ, hoặc dựa trên giả định kém.
- **Lỗi chìm**: hệ thống chạy sai mà **cả người dùng lẫn hệ thống đều không nhận ra**. Với một trợ lý có quyền ghi sổ, đây là loại nguy hiểm nhất: người chịu hại thường là bên thứ ba.

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 |
|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 |
|---|---|---|
| Vì sao người gặp coi đây là lỗi | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | |

**Ví dụ (bộ nền, đừng chép):** `T-002@55` · sổ cái có dòng hoàn 20.000đ, hãng VNX nhận một lỗi, trong khi tracking ghi trễ 2 ngày ·
khách không thấy gì sai, hãng chịu · cao · **lỗi chìm**. Nguồn: đầu vào (đặt sai trọng số cho con số khách tự khai). Xử lý:
hãng coi là lỗi vì sổ giao của họ ghi 2 ngày; kiểu giải pháp: trao quyền cho người (số khai khác tracking thì chuyển người duyệt);
tín hiệu: đếm sự kiện `model_override` mỗi ngày.

---

<a id="b3"></a>

## B3 · Câu 2.3 · Bản đồ dữ liệu của trợ lý và ví dụ drift

**Cách làm:** đi từ người dùng và việc họ cần làm, tới đầu ra của hệ thống, rồi mới hỏi hệ thống cần dữ liệu
gì, định dạng ra sao, và **thế giới thật làm dữ liệu đó lệch đi thế nào**; cuối cùng tóm lại trong vài câu.
Trợ lý LogiX không huấn luyện gì trong lab này, nên ta hỏi về "dữ liệu trợ lý đọc lúc chạy / trường then chốt / nguồn sự thật".
Gợi ý: mở `data/world.json` phần `policies`, `orders[].parcels`, `ops_limits`, `ops_facts`.

| Mục | Điền cho trợ lý hoàn tiền |
|---|---|
| Người dùng | |
| Việc người dùng cần làm xong | |
| Đầu ra của hệ thống (kể cả các lệnh ghi) | |
| Dữ liệu trợ lý đọc lúc chạy (bảng nào trong `data/world.json`) | |
| Trường then chốt quyết định tiền và lỗi hãng | |
| Với mỗi trường then chốt: **nguồn sự thật** hay **bản sao** (ai cập nhật, khi nào)? | |
| Định dạng cần để ý (ngày, trường được phép trống, đơn nhiều kiện) | |
| Thế giới thật làm dữ liệu lệch ở đâu (theo mùa, đổi chính sách, giờ cao điểm, người nhập tay)? | |
| Câu người ngoài sẽ hỏi về nguồn dữ liệu ("sao hệ thống biết đơn trễ mấy ngày?") | |

**Tóm lại (điền vào chỗ trống):**
Trợ lý dùng `__________`, `__________`, `__________` để giúp `__________` làm được `__________`.
Trường mà nếu sai thì tiền hoặc lỗi hãng sai theo: `__________`, `__________`.
Chúng tôi biết thế giới thật sẽ làm dữ liệu lệch ở: `__________`. Dấu hiệu nhìn thấy sớm nhất: `__________`.

**Ví dụ drift trong 3 tháng tới** (lấy từ dòng "thế giới thật làm dữ liệu lệch"): cái gì đổi `____` · đổi ngày nào `____` ·
trường nào cho thấy `____` · con số nào của Bản tiêu chí bị ảnh hưởng `____`.
Đây là đầu vào đổi hay quan hệ vào–ra đổi? Chỉ số nào sẽ phát hiện? `__________`

**Ví dụ một dòng (đừng chép):** trường then chốt `parcels[].delivered_date` · bản ghi do máy quét ở điểm phát tạo ra, là nguồn
sự thật về ngày giao · lệch khi điểm phát quét sót hoặc nhập bù bằng tay.

---

<a id="b4"></a>

## B4 · Câu 2.4 · HAZOP vòng 1 trên tool của agent

*Chỉ làm MỘT vòng, trên MỘT tool. Đây là HAZOP vòng 1; HAZOP của thẻ sự cố viết riêng ở Phiếu C mục C4, không ghi đè bảng này.*

**Khung tư duy.** HAZOP không hỏi "cái gì có thể hỏng" một cách chung chung. Nó cầm từng **từ gợi ý** áp vào từng **dòng dữ
liệu đi vào một hành động** và hỏi: nếu dòng này lệch theo kiểu đó thì hậu quả là gì, ai chịu. Mục tiêu là tìm ra những nhánh
mà cả bàn chưa nghĩ tới, không phải tả lại nhánh đã biết.

| Guideword | Nghĩa khi áp vào một tool của agent |
|---|---|
| **WRONG** | Giá trị đưa vào có đủ, hợp lệ về hình thức, nhưng sai sự thật |
| **INVALID** | Giá trị không còn hiệu lực: hết hạn, sai phiên bản, sai đối tượng |
| **INCOMPLETE** | Thiếu một phần thông tin cần có để quyết định |
| **PERTURBED** | Đầu vào bị ai đó cố ý hoặc vô tình làm lệch (cài câu lệnh, gửi lặp) |
| **INCAPABLE** | Thành phần không trả lời được: quá tải, lỗi, hết quota |

**Câu hỏi dẫn dắt:** tool nào tạo ra hậu quả không đảo ngược? Mỗi tham số của tool đó lấy từ đâu (ticket, DB, model tự suy)?
Với mỗi guideword: hậu quả cho ai, hiện có gì ngăn, cần thêm gate ở tầng nào (phát hiện / chặn / giới hạn thiệt hại)?

Tool chọn phân tích: `file_carrier_fault` (ghi lỗi hãng, có thể làm đối tác bị phạt hoặc mất quyền nhận chuyến).

Người phân tích: Lê Viết Khoa, thành viên 3. Các dòng dưới là phân tích tĩnh trước khi đo, chưa phải lỗi đã xác nhận bằng trace. Dữ kiện: `lab10/agent.py` phần tracking/policy/fail_open/ghi lỗi, `lab10/tools.py` hàm `file_carrier_fault`, `data/world.json` mục `carriers`, `policies`. Sau khi ký và đo baseline, thành viên 2 bổ sung ticket@seed và xác nhận ít nhất một nhánh chưa xuất hiện trên trace đã xem.

| Tham số / dòng dữ liệu | Guideword | Lệch cụ thể (viết bằng dữ kiện của lab) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `parcel_id`, `carrier_id`, `driver_id` | WRONG | Agent chọn kiện trễ nhất để tính tiền nhưng lấy `parcels[0]` để ghi lỗi. Nếu kiện đang được xử lý không phải kiện đầu, đơn nhiều kiện có thể bị quy trách nhiệm sai. | Hãng/tài xế không gây trễ bị ghi lỗi; kế toán phải điều chỉnh đối soát. GHSH bị phạt 150.000đ/lỗi và có thể bị đình chỉ khi đủ 3 lỗi/7 ngày. | Guard hiện cho qua; công tắc đang bật. Chưa có đối chiếu đầy đủ giữa kiện có căn cứ và tham số ghi. | `write_gate` nhánh `file_carrier_fault`: xác định đúng kiện và hãng từ tracking, thiếu căn cứ thì chuyển người; tầng chặn. Chờ thành viên 2 triển khai và đo. |
| Chính sách dùng để xác định nguyên nhân chịu lỗi | INVALID | `index_active` có thể không còn khớp ngày hiệu lực. REFUND-v4 có hiệu lực 2026-12-01 và không coi FORCE_MAJEURE là lỗi hãng, khác v3. Đây là giả thuyết drift, chưa phải kết quả chạy. | Hãng bị ghi lỗi theo quy định hết hiệu lực dù vẫn phải hoàn phí cho khách. | Agent chọn chính sách bằng cờ index; cổng legal hiện false. | Dùng chính sách theo ngày hiệu lực; đề xuất `legal.carrier_fault_requires_recorded_cause=true` và guard kiểm chính sách tương ứng; tầng chặn. |
| `delay_cause` của kiện | INCOMPLETE | Tracking thiếu nguyên nhân, nhưng agent thay bằng CARRIER nếu có trễ. Không biết nguyên nhân bị biến thành kết luận lỗi hãng. | Hãng/tài xế gánh lỗi khi chưa có chứng cứ; tăng khiếu nại và sai sổ. | Khi legal gate false, không bắt buộc nguyên nhân được ghi trong dữ liệu kiện. | Bật `legal.carrier_fault_requires_recorded_cause`; không ghi khi thiếu nguyên nhân, chuyển người xác minh nếu cần; tầng chặn và vận hành. |
| `delay_days` đi vào quyết định ghi lỗi | PERTURBED | Khách tự khai số ngày và agent có nhánh `model_override` lấy số đó thay tracking. Một đơn chưa đủ điều kiện có thể bị biến thành đủ điều kiện hoàn và ghi lỗi. | LogiX chi sai; hãng bị ghi lỗi theo lời khách chưa kiểm chứng. | Agent có tracking nhưng vẫn cho phép ghi đè; guard hiện cho qua. | Guard đối chiếu điều kiện hoàn/ghi lỗi với tracking DB; log chênh lệch để điều tra, không quyết theo câu chữ/mã ticket; tầng chặn và phát hiện. |
| Kết quả kiểm chính sách khi LLM lỗi | INCAPABLE | `policy_check` lỗi liên tiếp thì agent đi nhánh `fail_open`, đặt tiền hoàn bằng phí giao và `do_fault=True`. | Có thể ghi lỗi hãng khi chưa kiểm được điều kiện; bên thứ ba chịu lỗi chìm. | Có retry nhưng hết retry vẫn cho tiếp tục; chưa có guard độc lập chặn nhánh suy giảm này. | Kỹ sư đặt cổng kiểm căn cứ xác định; khi thiếu căn cứ thì chuyển NV-HANH, không tự suy ra hãng có lỗi; tầng chặn. Cần đo tải chuyển người. |

Không bắt buộc điền đủ năm dòng. Bắt buộc: **ít nhất ba dòng, trong đó một dòng là nhánh bàn chưa thấy trên trace**.

**Mở rộng ra ngoài kỹ thuật (thêm ít nhất hai dòng):** "thành phần" không chỉ là model và tool. Áp cùng năm từ gợi ý vào:

| Thành phần ngoài code | Ví dụ câu hỏi |
|---|---|
| **Người duyệt** (vận hành) | INCAPABLE: chỉ một người trực mà 14 ca tới trong một giờ thì ca cuối chờ bao lâu? |
| **Ngân sách** (kinh doanh) | WRONG: tổng hoàn tự động trong ngày vượt mức Finance cho phép mà không ai được báo thì sao? |
| **Phạm vi pilot** (kinh doanh) | INVALID: có nhóm ticket nào trợ lý luôn phải chuyển người, tức là tự động hoá vô nghĩa? |
| **Dữ liệu gửi bên thứ ba** (pháp lý) | PERTURBED: chữ khách tự gõ có tên, số điện thoại người khác bị chép sang hãng thì ai chịu? |

| Thành phần | Guideword | Lệch cụ thể | Hậu quả, cho ai | Cổng đề xuất: code hay con số nào trong `config/operating_gates.json` |
|---|---|---|---|---|
| Người duyệt | INCAPABLE | Giả định stress: 14 ca cần duyệt đến đồng thời, 1 người xử lý 6 ca/giờ; ca cuối bắt đầu sau khoảng 130 phút, vượt SLA 60 phút. Không phải lưu lượng đã đo của lab. | Khách chờ lâu; NV-HANH bị quá tải; xử lý vội làm tăng sai sót. | Đề xuất ca ban đầu 1 người/6 ca giờ, cảnh báo chờ trên 30 phút; NV-TUNG điều phối hỗ trợ hoặc thu hẹp `business.pilot_scope`. Chốt số người bằng report, không khai công suất vượt `số người × 6`. |
| Ngân sách và trách nhiệm đối soát | WRONG | Chỉ nhìn tiền máy dưới 1.500đ/ticket mà bỏ công duyệt 10.000đ/ca và phí trực 30.000đ/người/ca; thêm người có thể làm tổng chi phí vượt làm tay. | LogiX lỗ; kế toán phải đối soát nhiều nhưng không tạo tiết kiệm. | Thành viên 1 chốt `business` và ngưỡng đã ký; kiểm tổng chi phí, ROI và từng kho trong report sau mỗi phương án nhân sự; tầng phát hiện và giới hạn phạm vi. |
| Dữ liệu gửi bên thứ ba | PERTURBED | `customer_note` chép nguyên ticket sang hãng; `recipient_contact` chứa tên/SĐT người nhận quà. Chặn khóa `phone` đơn lẻ không loại dữ liệu nằm trong hai khóa này. | Người mua/người nhận quà bị lộ thông tin dù không trực tiếp làm việc với trợ lý. | Đề xuất chặn `customer_note`, `recipient_contact` bằng `legal.pii_fields_blocked_to_third_party`; kiểm payload theo allowlist của chính sách trước gửi. TV2 xác nhận bằng trace; TV3 điều phối khiếu nại. |

**Ví dụ mẫu (`issue_refund`, đừng chép):** tham số `amount_vnd` · WRONG · số tiền tính từ số ngày khách tự khai · LogiX mất
tiền, hãng bị kéo theo một lỗi · hiện chỉ có trần "không vượt tổng tiền đơn" · cổng ghi so với quyền lợi tính từ DB (chặn).

---

<a id="b5"></a>

## B5 · Câu 2.4 · Checklist go-live 9 nhóm việc, lần 1

Checklist chín nhóm việc phải xong trước khi chạy thử thật. Bàn điền lần đầu ở đây, rồi cập nhật sau sự cố ở Phiếu C mục C11.
Cột "Bằng chứng lấy từ đâu" trỏ tới mục bàn đã điền ở bước khác; không điền thêm phiếu nào chỉ để lấp cột này.

Trạng thái: **Xong** (có bằng chứng) · **Chưa** · **Không áp dụng** (ghi lý do). Bằng chứng là **mã lần chạy**, tên file / mục phiếu, hoặc số trong report.
**Cột PIC bắt buộc:** mỗi dòng một người có tên (không ghi "cả bàn"). Dòng nào chưa có PIC thì coi như Chưa.

| # | Nhóm việc | Bằng chứng lấy từ đâu (đã có sẵn trong lab) | Mục cần kiểm tra | Trạng thái | Bằng chứng | PIC |
|---|---|---|---|---|---|---|
| 1 | Chất lượng | Report `lab10.eval` (mã lần chạy) + bảng soát lỗi (Phiếu B mục B2) | Đo sau khi ký; pass_rate/pass^k, lỗi chìm và regression có bằng chứng. | Chưa | Chờ report base, trace T-002@55 và report sau cổng; chưa chạy đánh giá. | Chờ họ tên thành viên 2 (phụ trách kỹ thuật) |
| 2 | Dữ liệu | Bản đồ dữ liệu (Phiếu B mục B3, câu 2.3): trường nào là nguồn sự thật, trường nào là bản sao | Tracking, chính sách hiệu lực, sổ cái, phê duyệt; tránh dùng cờ đối soát cũ thay sổ cái. | Chưa | Chờ TV1 điền B3 và cung cấp PRD/eval card Lab 9 đã chọn. | Chờ họ tên thành viên 1 |
| 3 | Bảo mật | Một vòng HAZOP với guideword PERTURBED (Phiếu B mục B4): chữ nào đi vào model mà không do LogiX viết | Dữ liệu khách và checkout note không được trở thành quyền sửa tiền, bên trả hay lỗi hãng. | Chưa | B4 đã phân tích tĩnh; chờ guard và behavioral test có trace ở B7.1/B7.3. | Chờ họ tên thành viên 2 |
| 4 | Quyền hạn | `config/switches.json` + guard trước lệnh ghi; thẻ S2, S8 có thêm mục mức kiểm soát (Phiếu C mục C3) | Vượt hạn mức cần phê duyệt đúng người, đúng đối tượng, chưa dùng/hết hạn; kiểm tra trước mỗi lệnh ghi. | Chưa | Mã nhân sự có trong world; công tắc đang on và guard còn cho qua. Chờ TV2 triển khai/kiểm chứng. | Chờ họ tên thành viên 2 |
| 5 | Hiệu năng, hạ tầng | Đội tự ước tính; HAZOP guideword INCAPABLE: LLM không trả lời thì sao; số người duyệt và số ca mỗi giờ | Kiểm tải chuyển người và kiểm lại; không để fail_open sinh lỗi hãng; SLA nhận xử lý 60 phút. | Chưa | B4 và B7.6 có giả định tải/công suất; chờ report xác nhận hàng chờ và phương án LLM lỗi. | Lê Viết Khoa |
| 6 | Chi phí | Khối "kinh doanh và vận hành" của report: chi phí mỗi ticket so với làm tay, ROI, tiền LLM ticket đắt nhất; `config/operating_gates.json` mục `business` | Tách tiền máy/công duyệt/phí trực; so 10.000đ làm tay và kiểm kho xấu nhất, không chỉ số trung bình. | Chưa | ops_facts có giá cơ sở; chờ TV1 chốt business và TV2 cung cấp report so sánh nhân sự. | Chờ họ tên thành viên 1 |
| 7 | Vận hành | Runbook (Phiếu B mục B7.5–B7.6) + `config/operating_gates.json` mục `operations` (PIC, người duyệt, số người trực, điều kiện dừng, kênh báo tin) + metric trong `monitors.py` | Người trực, thẩm quyền dừng, kênh liên lạc và ngưỡng phải khớp config/report; có thời hạn dừng. | Chưa | B7.5–B7.6 là đề xuất chưa áp dụng; chờ baseline, chốt phạm vi, kênh thực tế và kiểm chứng tải. | Lê Viết Khoa |
| 8 | Con người, pháp lý | Bên thứ ba (hãng, tài xế, shop, người nhận quà, người đứng tên duyệt); `config/operating_gates.json` mục `legal`; thẻ S6, S7, S8 có mục riêng ở Phiếu C mục C3 | Loại dữ liệu không cần thiết khi gửi hãng; ghi lỗi đúng kiện/nguyên nhân; có đầu mối tiếp nhận phản hồi. | Chưa | A2, B4 và B7.5 đã có thiết kế; chờ áp dụng legal đúng bước và trace xác nhận. Chưa nhận thẻ. | Lê Viết Khoa |
| 9 | Quyết định | Câu tiêu chí (Phiếu A mục A4) + hash Bản tiêu chí đã ký + quyết định Gate 1 (Phiếu B mục B8, Phiếu C mục C12) | Ký/commit/push trước đo; chốt vòng 1; quyết định có run_id và khớp mọi ngưỡng bắt buộc. | Chưa | Chờ TV1 chốt/ký tiêu chí và cả nhóm quyết v1/v2 sau khi có report. | Chờ họ tên thành viên 1 |

Ô "Chưa" có rủi ro cao → chuyển thành một dòng Risk register (Phiếu C mục C10).

---

<a id="b6"></a>

## B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa (khoảng 8–10 phút, cả bàn)

*Mọi bàn làm pre-mortem ở vòng 1, TRƯỚC khi biết sự cố, để chọn 2–3 cổng phòng ngừa sẽ dựng. Ở vòng 2 bàn mở lại phần này ở
Phiếu C mục C1 (bút khác màu).*

**Khung tư duy.** Hỏi "có rủi ro gì không" thì ai cũng dè dặt. Nói "nó đã hỏng rồi, vì sao" thì mọi người được phép nói ra
điều mình vẫn lo. Làm im lặng trước, đọc sau, để ý kiến của người nói to không lấn át.

**Đề bài (đọc to):** *"Ba tháng sau pilot, LogiX phải tắt trợ lý hoàn tiền ở cả hai depot. Chuyện gì đã xảy ra?"*

1. **2 phút, im lặng:** mỗi người viết 2 lý do, mỗi lý do một dòng.
2. **2 phút:** đọc vòng tròn, mỗi lượt một lý do, không bình luận. Gộp lý do trùng.
3. **2 phút:** xếp từng lý do vào một **lăng kính**. Lăng kính nào còn trống thì cả bàn viết thêm ít nhất một lý do cho nó.
4. **2 phút:** chọn 2–3 lý do sẽ biến thành **cổng phòng ngừa** ngay hôm nay (code trong `guards.py` hoặc con số trong
   `config/operating_gates.json`). Lý do còn lại → Risk register.

Bốn lăng kính (bắt buộc đủ cả bốn; dự án AI hay chết ở ba lăng kính sau hơn là ở lăng kính đầu):

| Lăng kính | Câu hỏi gợi ý trên LogiX |
|---|---|
| **Kỹ thuật** | Model tin nhầm cái gì? Dữ liệu nào thiếu, cũ, lệch? Lệnh ghi nào không đảo ngược được? |
| **Kinh doanh** | Mỗi ticket tốn bao nhiêu so với làm tay? Một ngày hoàn tối đa bao nhiêu? Nhóm ticket nào không thể có lời? |
| **Con người và vận hành** | Ai duyệt, mấy người, mỗi giờ được mấy ca? Lượng việc tăng gấp ba thì sao? Nhân viên có tin trợ lý không? |
| **Pháp lý** | Dữ liệu cá nhân của ai rời hệ thống? Bên thứ ba nào bị ghi lỗi, bị trừ tiền mà không được hỏi? |

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được hôm nay? (trace / data / config nào) | Thành cổng phòng ngừa nào (code hay config) / hay vào risk register |
|---|---|---|---|
| | Kỹ thuật | | |
| | Kinh doanh | | |
| Trợ lý đã chuyển quá nhiều ca sang một người duyệt và nhân viên phải kiểm lại quyết định thiếu giải thích; hàng chờ vượt 60 phút nên pilot bị dừng. (Đóng góp TV3, chờ thảo luận nhóm.) | Con người và vận hành | `ops_facts`, `staff_behavior`; sau khi ký đo `ops.queue.wait_max_min`, `stuck`, `recheck_pct`, `trust`. | Đề xuất `operations` ở B7.5, runbook giờ cao điểm B7.6; cần cân đối tải và chi phí, không chỉ tăng số người. |
| Thông báo gửi hãng đã chứa nguyên văn ticket hoặc thông tin người nhận quà; đồng thời hãng bị ghi lỗi khi chưa có nguyên nhân được xác nhận. (Đóng góp TV3, chờ thảo luận nhóm.) | Pháp lý | `agent.py` payload gửi hãng; `tools.py` legal gate; chính sách `carrier_notice_fields`. Chờ trace sau ký. | Đề xuất chặn `customer_note`, `recipient_contact`; yêu cầu nguyên nhân theo chính sách hiệu lực; TV2 kiểm thêm đúng kiện/hãng. |
| | | | |

---

<a id="b7"></a>

## B7 · Khối 2B · Cổng phòng ngừa (phút 85–105)

### B7.1 · Câu 2.6 · 2–3 cổng phòng ngừa trong `lab10/guards.py`

Mỗi cổng ứng với một dòng pre-mortem (B6) hoặc một dòng HAZOP (B4). Viết trong `pre_guard(ctx)` (trước khi trợ lý đọc ticket)
hoặc `write_gate(ctx, action)` (trước mỗi lệnh ghi). Thử bằng:

```bash
python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."
python3 -m unittest discover -s tests
```

| # | Cổng (hàm và nhánh, ví dụ `write_gate` khi `tool == "issue_refund"`) | Ứng với dòng nào ở B6 / B4 | Chặn điều gì, dựa vào nguồn sự thật nào | Mã lần chạy `base · after` | Ca đang đúng nào bị hỏng? (phải là "không") |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### B7.2 · Câu 2.7 · Hai bước tránh rò rỉ dữ liệu

Bàn đang chỉnh cổng tới khi 22 ticket bộ nền xanh hết. Nêu 2 bước cụ thể để không "chỉnh trên chính bộ dùng để chấm"
(gắn với bộ nền, gói sự cố, bài kiểm tra ẩn):

1. …
2. …

### B7.3 · Câu 2.8 · Một behavioral test

- Tính chất (một câu): …

```bash
python3 -m lab10.trace --suite base --stage after --adhoc "..." --order O-10xx --customer C-xx
```

| Ticket hiểm | Nội dung ticket (`--adhoc`) | `--order` · `--customer` | Kết quả (dán dòng `SỔ CÁI` / `LỖI HÃNG` / `GỬI HÃNG`) | Tính chất giữ được? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

Giữ hai ticket này cho phần demo.

### B7.4 · Câu 2.9 · Cổng kinh doanh (`config/operating_gates.json` mục `business`)

Mỗi con số kèm một câu lý do, lấy từ `data/world.json` → `ops_limits`, `ops_facts`.

| Khoá | Giá trị bàn đặt | Lý do (một câu, có số) |
|---|---|---|
| `business.daily_refund_cap_vnd` | | |
| `business.cost_budget_per_ticket_vnd` | | |
| `business.pilot_scope` (all / warehouse / percent) | | |
| `business.roi_min` | | |

### B7.5 · Câu 2.10 · Cổng con người, vận hành, pháp lý + Runbook phần 1–3

Điền `config/operating_gates.json` mục `operations` và `legal` (PIC, người duyệt, số người trực mỗi ca, công suất duyệt mỗi giờ,
thời gian chờ tối đa, điều kiện dừng, kênh báo tin; trường dữ liệu cá nhân không gửi cho bên thứ ba; ghi lỗi cho hãng phải có
nguyên nhân trong tracking). Rồi viết runbook dưới đây **khớp với các con số đó**.

*Runbook là tờ giấy người trực ca cầm lúc 23h khi có chuyện. Nó trả lời: nhìn con số nào, ngưỡng nào thì làm gì, ai được quyết.
Phần 1–3 và mục Giờ cao điểm viết ở vòng 1. Phần 4–5 viết ở vòng 2 (Phiếu C mục C11). Mọi con số phải khớp `config/operating_gates.json` và report.*
*Mỗi phần trả lời bốn câu hỏi: ai chịu trách nhiệm, nhìn gì, ngưỡng nào, làm gì.* **Người viết (vai Vận hành và pháp lý):** Lê Viết Khoa — 2A202603737

**Trạng thái: đề xuất chuẩn bị trước, CHƯA áp dụng vào config và CHƯA được nhóm chốt.** Theo trình tự lab, phải ký/commit/push tiêu chí, đo baseline và hoàn thành khối 2A trước khi sửa config ở khối 2B. Chờ TV1 xác nhận tiêu chí, phạm vi, kênh liên lạc; chờ TV2 cung cấp report. Không dùng phần này để tuyên bố cổng đã hoạt động. Khi chốt cần cập nhật đồng thời bảng dưới, config và bằng chứng report.

| Khóa config | Đề xuất vòng 1 để thảo luận | Căn cứ / phần còn chờ |
|---|---|---|
| `operations.pic` | `NV-TUNG` | Lê Thanh Tùng là giám sát vận hành, giữ công tắc trong `staff`. |
| `operations.approver_id` | `NV-HANH` | Trần Thị Hạnh là trưởng ca, có quyền duyệt hoàn vượt hạn mức; khai mã không thay kiểm tra hiệu lực từng phê duyệt. |
| `operations.reviewers_on_shift` | `1` ban đầu | Có sẵn 1 người/ca theo ops_facts; chưa chứng minh đủ tải. Chờ report để chốt. |
| `operations.review_capacity_per_hour` | `6` | Tổng công suất 1 người × 6 ca/giờ; không khai vượt năng lực thực. |
| `operations.max_queue_wait_minutes` | `60` | SLA tiếp nhận trong ops_limits là 60 phút. Đề xuất cảnh báo sớm trên 30 phút. |
| `operations.stop_conditions` | Trên 60 phút chờ hoặc có ca ùn: thu hẹp tải; có ghi lỗi oan/lộ dữ liệu/hoàn sai: dừng thao tác liên quan và kiểm tra theo runbook 3. | Ngưỡng an toàn 0 sự kiện là đề xuất, phải thống nhất với tiêu chí TV1 trước khi ký. Đây là câu quy trình, không tự thi hành dừng. |
| `operations.alert_channel` | `OPS-PILOT-GATE1` (tên đề xuất) | Chưa có kênh thật; nhóm cần xác nhận nền tảng, người nhận và cách gọi khẩn. Config không tự gửi tin. |
| `operations.decision_note` | `true` | Có ghi chú thì một lần kiểm lại tốn 0,4 đơn vị thay vì 1; thêm 100đ cho quyết định refunded/denied theo giá mock. Chờ kiểm chứng tổng chi phí. |
| `operations.review_sampling_pct` | `10` | Mức tối thiểu trong trust_conditions là 10%; còn cần đúng approver, ghi chú và không có phê duyệt sai. Chưa bảo đảm monitor bắt mọi lỗi. |
| `legal.pii_fields_blocked_to_third_party` | `["customer_note", "recipient_contact"]` | Đây là hai khóa payload thực tế chứa văn bản khách và liên hệ người nhận. Bộ lọc chỉ loại khóa cấp ngoài; TV2 cần kiểm payload còn lại. |
| `legal.carrier_fault_requires_recorded_cause` | `true` | Chỉ ghi khi kiện có nguyên nhân thuộc fault_causes của chính sách hiệu lực. Còn cần guard kiểm đúng kiện/hãng/độ trễ. |

#### Runbook 1 · Ai chịu trách nhiệm

| Vai | Tên / mã nhân viên (lấy từ `data/world.json` → `staff`) | Được quyền làm gì | Liên lạc qua kênh nào |
|---|---|---|---|
| PIC của trợ lý (một người) | Đề xuất: Lê Thanh Tùng — `NV-TUNG` | Chịu trách nhiệm sự cố; quyết định tạm dừng, điều phối người và phạm vi pilot trong giới hạn nhóm phê duyệt. | Đề xuất OPS-PILOT-GATE1; chờ nhóm xác nhận kênh thực và cách gọi khẩn. |
| Người duyệt đứng tên các khoản vượt hạn mức | Trần Thị Hạnh — `NV-HANH` | Duyệt từng khoản trong thẩm quyền; yêu cầu đúng ticket/đơn/khách, số tiền, hạn và trạng thái phê duyệt. Không dùng lại mã duyệt sai đối tượng. | Kênh vận hành đề xuất ở trên; chưa triển khai. |
| Người giữ công tắc tắt từng thao tác ghi | Lê Thanh Tùng — `NV-TUNG` | Dừng hoàn tiền, ghi lỗi hoặc gửi hãng theo phạm vi sự cố; yêu cầu kỹ sư triển khai đường chặn và kiểm chứng. | Gọi khẩn NV-TUNG; chờ nhóm chốt cách liên lạc dự phòng. |
| Người nhận khiếu nại của bên thứ ba (hãng, shop, người nhận quà) | Đề xuất: Phạm Kiều Oanh — `NV-OANH` | Tiếp nhận, đối soát tiền/lỗi hãng, phối hợp NV-HANH xử lý khách/người nhận; không chuyển tiếp thêm PII khi báo sự cố. Vai tiếp nhận cần nhóm xác nhận. | Chuyển ticket nội bộ tới NV-OANH, báo PIC qua kênh được nhóm xác nhận. |

Số người trực duyệt mỗi ca: đề xuất 1 · Mỗi giờ duyệt được: đề xuất tổng 6 ca · Phạm vi pilot: CHỜ TV1 chọn kho hoặc tỷ lệ và đường xử lý ticket ngoài phạm vi. Không diễn giải mode all mặc định là phạm vi nhóm đã phê duyệt.

#### Runbook 2 · Nhìn con số nào, ngưỡng nào thì làm gì

Mỗi dòng một tín hiệu. Cột "Lấy ở đâu" phải là một dòng trong report của `lab10.eval` / `lab10.grade` hoặc một chỉ số trong `lab10/monitors.py`.

| Tín hiệu | Lấy ở đâu | Bình thường | Ngưỡng VÀNG → việc làm | Ngưỡng ĐỎ → việc làm | Ai quyết |
|---|---|---|---|---|---|
| Thời gian chờ người duyệt lâu nhất | Report `ops.queue.wait_max_min`; chưa có giá trị đo. | Đề xuất ≤30 phút. | >30 đến 60 phút: NV-HANH kiểm tra backlog, báo NV-TUNG chuẩn bị hỗ trợ. | >60 phút: vượt SLA, ngừng tăng tải, thu hẹp phạm vi hoặc chuyển luồng thủ công đã có người nhận. Không nâng SLA để làm xanh report. | NV-TUNG, phối hợp NV-HANH. |
| Số ca bị ùn | Report `ops.queue.stuck` (tối đa theo seed); chưa đo. | Đề xuất 0 ca. | Chưa ùn nhưng chờ >30 phút: xử lý sớm như dòng trên. | >0 ca: ưu tiên ca cũ; kiểm tải chuyển người và kiểm lại; chưa kết luận đủ điều kiện Tiếp tục. | NV-TUNG. |
| Chi phí mỗi ticket so với làm tay | `ops.cost.cost_per_ticket_vnd`, `roi`, `llm_cost_max_per_ticket_vnd`; theo kho ở `ops.segments`. | Tổng chi phí dưới ngưỡng đã ký và không vượt làm tay 10.000đ; ROI đạt ngưỡng đã ký. | Đề xuất tổng chi phí ≥8.000đ nhưng chưa vượt ngưỡng đã ký: TV1 và PIC xem nguyên nhân, nhất là công duyệt/phí trực. Nếu ngưỡng ký thấp hơn 8.000đ, dùng cảnh báo ở 80% ngưỡng thấp hơn. | Tổng chi phí >10.000đ hoặc vượt ngưỡng đã ký, ROI dưới ngưỡng hoặc tiền máy >1.500đ: không chọn Tiếp tục; đánh giá từng kho và thu hẹp/cải tiến theo decision_rule. | NV-TUNG cùng vai Sản phẩm và kinh doanh. |
| Tổng tiền hoàn tự động trong ngày so với trần | `ops.refund.auto_refund_day_max_vnd`, `finance_daily_budget_vnd`, `team_daily_cap_vnd`. | Dưới 80% C, với C = min(2.000.000đ, trần ngày TV1 chốt). Chờ giá trị C. | Đạt 80% C: NV-OANH kiểm tra tốc độ chi, báo PIC. | Khoản tiếp theo làm vượt C phải chuyển người trước khi ghi; nếu report đã vượt C thì dừng hoàn tự động và đối soát. Chờ TV1 đặt cap và TV2 xác nhận cổng thực thi. | NV-TUNG; NV-OANH đối soát, NV-HANH duyệt. |
| Tiền hoàn sai | Report `wrongful_refund_vnd`, `ops.refund.wrongful_refund_worst_day_vnd`; các số này cần nhãn trong lab. | Đề xuất 0đ; chờ TV1 chốt trước ký. | Có khiếu nại/chênh lệch đối soát chưa xác nhận: giữ ca liên quan để người kiểm. Không coi tín hiệu này đã được tự động hóa. | Có khoản hoàn sai được xác nhận hoặc số report vượt ngưỡng đã ký: tạm dừng `issue_refund`, đối soát toàn bộ phạm vi liên quan. | NV-TUNG dừng; NV-OANH đối soát. |
| Lỗi ghi oan cho hãng / lộ dữ liệu cá nhân (pháp lý) | Report `wrongful_carrier_faults`, `pii_leaks` trong lab; production dùng phản hồi/đối soát và telemetry A2, không có nhãn sẵn. | Đề xuất 0 sự kiện; chờ TV1 chốt. | Có phản ánh hoặc thông báo ngoài allowlist: bảo toàn log trong hệ thống nội bộ, chuyển PIC xác minh ngay. | Xác nhận ≥1 lỗi oan hoặc lộ PII: dừng ghi lỗi/gửi hãng tương ứng, khoanh vùng và liên hệ bên bị ảnh hưởng qua đầu mối. Nếu telemetry A2 ≥1 thì tạm dừng gửi để điều tra ngay dù chưa xác nhận lộ PII. | NV-TUNG; NV-OANH/NV-HANH xử lý bên bị ảnh hưởng. |
| Lòng tin và khối lượng kiểm lại | Report `ops.queue.trust`, `trust_why`, `recheck_pct`; không phải monitor mới của vòng 2. | Trust không báo chưa đạt; tỉ lệ kiểm lại theo phương án đã thống nhất. | Nhân viên kiểm lại nhiều hơn kế hoạch: kiểm ghi chú, approver và tính hợp lệ phê duyệt trước khi tăng người. | Trust chưa đạt kèm quá tải/vi phạm: chặn nguyên nhân quyền hạn, điều chỉnh quy trình; không ép giảm kiểm lại khi chưa sửa lỗi. | NV-HANH báo, NV-TUNG điều phối. |

Các ngưỡng trên là phương án vận hành trước đo. `stop_conditions`/`alert_channel` chỉ ghi quy trình; cảnh báo và công tắc không tự được triển khai bởi bảng này. Cần đưa các ngưỡng chấp nhận liên quan vào Phiếu A trước khi ký. Chưa có report để xác nhận bất kỳ dòng nào đạt.

#### Runbook 3 · Điều kiện dừng và cách dừng

- Dừng một phần (tắt một thao tác ghi, thu hẹp phạm vi) khi: theo đề xuất, phát hiện ghi lỗi oan thì dừng ghi lỗi hãng liên quan; nghi lộ PII thì tạm dừng `notify_carrier`; hoàn sai/phê duyệt không hợp lệ thì dừng `issue_refund`; chờ >60 phút hoặc có ca ùn thì giảm tải pilot. Cổng nào còn hở và phạm vi nào an toàn phải được kỹ sư chứng minh; chưa có kết quả đo.
- Dừng hẳn khi: không xác định được phạm vi ảnh hưởng, không thực hiện được việc chặn riêng thao tác nguy hiểm, hoặc tiếp tục có tác hại sau khi đã dừng một phần. Chờ nhóm thống nhất với `stop_condition` và `decision_rule` trước ký; đây chưa phải quyết định Gate 1.
- Cách dừng, từng bước (công tắc nào trong `config/switches.json`, dòng nào trong `config/operating_gates.json`): (1) NV-HANH/NV-OANH báo PIC kèm ticket và dấu hiệu, không phát tán lại PII. (2) NV-TUNG xác định thao tác/phạm vi cần dừng. (3) Trong hệ thống vận hành, công tắc tương ứng là `issue_refund`, `file_carrier_fault`, `notify_carrier`, `send_reply` = off; chặn đầu vào khi dừng toàn bộ. Trong bài lab, guide yêu cầu giữ nguyên `switches.json`: TV2 phải hiện thực đường chặn trong vị trí được phép `guards.py`, và chỉ chỉnh `business.pilot_scope` khi có quyết định phạm vi. Không nộp phương án scope=0 như một cách sửa đạt. (4) Kiểm tra bằng trace có ticket phù hợp và log để xác nhận không còn lệnh ghi nguy hiểm. (5) Ghi lại thời điểm, người thực hiện, ticket bị giữ và kế hoạch phục hồi. Đường dừng hiện chưa được TV2 triển khai/kiểm chứng.
- Từ tín hiệu đỏ đến lúc dừng xong tối đa 5 phút (mục tiêu đề xuất, chưa được đo hoặc nhóm phê duyệt); người bấm/quyết định vận hành: NV-TUNG; kỹ sư thực thi trong lab: chờ họ tên TV2. Nếu chưa có đường dừng được kiểm chứng thì mục vận hành vẫn Chưa.
- Khi đã dừng, ticket đang chờ đi đâu, ai xử lý: hàng chờ nội bộ do NV-HANH phân công, NV-OANH ưu tiên các ca cần đối soát tiền/lỗi hãng; lưu rõ ca đã ghi tiền trước khi chuyển người để không hoàn lại lần nữa. Giữ thứ tự và thời điểm nhận. Không chuyển vô hạn sang chính một người đang quá tải; thiếu năng lực thì PIC báo thời gian chờ và dừng nhận thêm vào pilot.
- Điều kiện để bật lại, ai ký: đã xác định nguyên nhân, sửa đúng nhánh, đối soát tác hại cũ; report hiện tại không còn vi phạm liên quan, regression đạt và hàng chờ trong SLA; guard/phạm vi chốt khớp runbook. NV-TUNG ký vận hành, NV-HANH xác nhận năng lực duyệt, NV-OANH xác nhận đối soát khi có tiền/lỗi hãng. Cả nhóm đối chiếu tiêu chí đã ký trước khi quyết Gate 1. Chưa có bằng chứng để bật lại ở thời điểm chuẩn bị.

### B7.6 · Giờ cao điểm (bắt buộc với thẻ S4; các thẻ khác nên có)

Lượng ticket có thể dồn gấp ba trong một giờ (ngày sale, sau bão). Viết trước, khi chưa biết sự cố.

| Câu hỏi | Trả lời (có số, có tên) |
|---|---|
| Giờ cao điểm là khi nào, bao nhiêu ticket mỗi giờ (dựa vào `ops_facts`)? | Giả định stress vào giờ sale/sau bão: lượng ticket tăng 3 lần trong một giờ. Chưa có lưu lượng thực; TV2 lấy `arrive_min` và tỷ lệ chuyển người/kiểm lại từ report để lập tải. Không suy lưu lượng từ năng lực 6 ca/giờ. Bài tính độc lập: 14 ca cần duyệt đến đồng thời với công suất 6 ca/giờ thì ca cuối chờ khoảng 130 phút. |
| Ai trực giờ cao điểm, mấy người (khớp `operations.reviewers_on_shift`)? | Đề xuất ban đầu NV-HANH phụ trách duyệt, 1 người/ca, tổng công suất 6 ca/giờ. NV-TUNG điều phối, NV-OANH đối soát; không tự tính hai người này là người duyệt bổ sung. Chờ nhóm xác nhận người dự phòng có thẩm quyền và report xác nhận phương án 1 người khả thi. |
| Ngưỡng nào thì **gọi thêm người** (hàng chờ bao nhiêu ca, chờ lâu nhất bao nhiêu phút)? Ai gọi? | Đề xuất khi >3 ca đang đợi hoặc ca lâu nhất >30 phút: NV-HANH báo NV-TUNG huy động người duyệt đã được phân quyền. Backlog tức thời chưa có trong report tổng hợp nên cần log hàng chờ khi chạy thật; chưa được coi là monitor đã triển khai. Chỉ đổi `reviewers_on_shift` khi có người thực nhận ca; tổng công suất không vượt số người × 6. |
| Ngưỡng nào thì **thu hẹp** phạm vi (khoá `business.pilot_scope`) hoặc **tắt** một thao tác ghi (`config/switches.json`)? Ai quyết? | Chờ >60 phút, có ca ùn hoặc dự báo tải duyệt vượt năng lực mà không có người hỗ trợ: NV-TUNG và vai sản phẩm chọn kho/tỷ lệ phù hợp, chỉ rõ đường thủ công cho ticket ngoài phạm vi. Tác hại pháp lý/tiền thì dừng riêng thao tác ngay theo runbook 3. Giữ nguyên switches.json trong bài nộp theo guide; đường chặn lab chờ TV2 hiện thực ở guards.py. Không thu hẹp về 0 để làm report xanh. |
| Thêm người thì chi phí mỗi ticket và ROI thay đổi thế nào (đọc report)? | Chưa có report nên chưa kết luận. Theo mô hình, phí trực = số người × 30.000đ/ca; từ 1 lên 2 người tăng 30.000đ/ca. Nếu N ticket/ngày trong phạm vi và các khoản khác giữ nguyên, phần phí tăng là 30.000/N đ/ticket. Tổng chi phí còn phụ thuộc số ca duyệt/kiểm lại; cần TV2 đo từng phương án và TV1 đối chiếu ROI/ngưỡng đã ký, kể cả từng kho. |

---

<a id="b8"></a>

## B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 (phút 105–115)

Làm đúng thứ tự:

```bash
python3 -m lab10.checkpoint
python3 -m lab10.eval --suite base --stage prepared
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

**Khung tư duy.** Gate 1 "đạt" khi **quyết định khớp bằng chứng và khớp tiêu chí đã ký trước**. Tiếp tục, Thu hẹp, Cải tiến
thêm, Dừng đều có thể là quyết định đạt. Quyết định không đạt là quyết định mà con số trong report không đỡ được.
Chỉ chọn Tiếp tục khi mọi chỉ số bắt buộc đều đạt.

Ba câu tự vấn trước khi viết: (1) Rủi ro còn lại có chấp nhận được như hiện trạng không? (2) Cần thêm biện pháp nào, tốn
bao nhiêu thời gian? (3) Có phần nào của dự án không nên làm tiếp?

| | **v1** (phút 105–115, TRƯỚC khi nhận thẻ sự cố) |
|---|---|
| Commit ký tiêu chí (message `Sign acceptance criteria`; hash commit, tuỳ chọn) | |
| Hash chốt cổng vòng 1 (8 ký tự lệnh `lab10.checkpoint` in ra, tuỳ chọn) | |
| Mã lần chạy dùng làm bằng chứng | bộ nền, mốc base: ________ · bộ nền với cổng vòng 1 (prepared): ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Đọc khối "theo kho và hãng" ở cuối output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt phần nào, vì sao | |
| Nếu Cải tiến thêm: giả thuyết cụ thể + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Một bằng chứng còn thiếu (thứ bộ nền chưa đo được) | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

Xong v1 thì lưu và đẩy một bản (sau mốc này không sửa cột v1):

```bash
git add lab10/guards.py lab10/guards_round1.py config/operating_gates.json config/operating_gates.round1.json config/round1.lock templates/form-b-evaluation-gates.md
git commit -m "LAB 10: chốt cổng vòng 1, quyết định v1"
git push -u origin main
```
