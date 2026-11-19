# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> …

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Mỗi khoản hoàn và khoản ghi lỗi hãng phải truy được về đúng đơn, kiện, bên trả tiền, chính sách và phê duyệt có hiệu lực; sổ cái không ghi trùng khi agent thử lại. Chị có thể đối soát với hãng và shop mà không phải tự dò và sửa các khoản do trợ lý ghi sai.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Nhận đúng các ca cần quyền quyết định của người, kèm căn cứ tracking, số tiền và lý do chuyển; tải duyệt nằm trong năng lực ca trực để ticket được nhận xử lý trong SLA 60 phút, và không có khoản vượt hạn mức tự động nào mượn danh chị bằng một phê duyệt không hợp lệ.

Ghi chú của Lê Viết Khoa (thành viên 3): mục tiêu dựa trên `data/world.json` mục `staff`, `ops_limits`, `ops_facts` và luồng ghi trong `lab10/agent.py`. Chờ thành viên 1 cung cấp PRD v1.1 Lab 9 đã chọn để đối chiếu các mục §2, §6; chưa xác nhận đã đối chiếu PRD.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | Nội dung thông báo đã gửi ra hãng qua `notify_carrier`, bảo vệ cả người mua và người nhận quà. |
| **Thước đo** (một câu, có đơn vị) | | Số thông báo gửi hãng có ít nhất một khóa payload ngoài danh sách được phép theo chính sách đang hiệu lực, đơn vị: thông báo/15 phút. Đây là tín hiệu nghi ngờ lộ dữ liệu, không phải nhãn xác nhận vi phạm. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | Toàn bộ thông báo `outbound` có `to` bắt đầu bằng `carrier:` trong cửa sổ; payload và ticket_id; danh sách `carrier_notice_fields` của chính sách có hiệu lực theo ngày. Trong mock: `world.outbound`, sự kiện tool `notify_carrier` và `data/world.json` mục `policies`; monitor được nhận `trial.outbound` không có nhãn. Không dùng `label`, `pass`, `pii_leaks` hay gán nhãn tay. Production cần log thời điểm gửi và phiên bản chính sách; mock chưa có timestamp từng thông báo nên chưa kiểm chứng cửa sổ 15 phút. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | Với mỗi thông báo gửi hãng m, so `set(m.payload.keys())` với tập A = `carrier_notice_fields` của chính sách hiệu lực. Cộng 1 nếu có khóa ngoài A, hoặc không xác định được payload/chính sách; mỗi thông báo chỉ đếm một lần. Đếm riêng ca thiếu dữ liệu để điều tra. Nếu cần tỷ lệ, chia số thông báo nghi ngờ cho tổng thông báo gửi hãng cùng cửa sổ; mẫu số 0 thì tỷ lệ là không áp dụng, không coi là bằng chứng an toàn. A hiện gồm `order_id`, `parcel_id`, `district`, `delay_days`; `customer_note` và `recipient_contact` nằm ngoài A. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Đề xuất trước khi đo: cửa sổ trượt 15 phút; từ 1 thông báo nghi ngờ thì báo NV-TUNG, tạm ngừng gửi hãng để kiểm tra; mục tiêu dừng trong 5 phút từ tín hiệu đỏ. Chờ cả nhóm chốt trước khi ký tiêu chí; chưa có cơ chế cảnh báo/dừng tự động được triển khai. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | Không phát hiện chắc chắn PII ẩn trong giá trị của khóa được phép, DB/chính sách sai, gửi nhầm hãng hoặc lỗi ghi oan. Chỉ thấy thông báo sau khi gửi nên không thu hồi được dữ liệu đã rời hệ thống. Cần bộ lọc trước gửi trong `legal` và kiểm tra cổng ghi; telemetry này chưa được cài vào `MONITORS`, cũng chưa có giá trị đo. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | | |
| `wrongful_refund_vnd_max` | | |
| `wrongful_carrier_faults_max` | | |
| `pii_leaks_max` | | |
| nên có: `escalation_rate_max` | | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): ____
- Ngưỡng chuyển cho người duyệt: ____

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Không dùng riêng pass_rate/pass^k để đại diện thành công. Khách cần được hoàn đúng và được tiếp nhận đúng hạn; hãng/tài xế cần không bị ghi lỗi oan; shop cần không bị trừ tiền sai; người nhận quà cần không lộ liên hệ; NV-HANH cần hàng chờ trong sức duyệt; NV-OANH cần sổ cái đúng và truy vết được. Do đó phải đọc đồng thời hoàn sai, lỗi hãng oan, PII, hàng chờ, chi phí/ROI và phân khúc kho/hãng; telemetry A2 chỉ phát hiện thông báo ngoài allowlist, không thay các kiểm tra này. Chờ TV1 chốt các câu tiêu chí ở Bước 1 để đối chiếu từng câu trước ký. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép giảm escalation_rate có thể khiến khách, shop và hãng chịu quyết định thiếu căn cứ; chuyển hết cho người có thể làm số an toàn đẹp hơn nhưng dồn tải và trách nhiệm sang NV-HANH, làm khách chờ quá SLA 60 phút. Ép giảm tiền máy có thể bỏ kiểm tra cần thiết; kiểm lại mọi quyết định hoặc thêm người không giới hạn làm mất tiết kiệm so với 10.000đ làm tay/ticket. Tối ưu số trung bình có thể che một kho/hãng bị hại. Cần giữ ranh giới quyền hạn, xem tải và chi phí theo phân khúc, ghi rõ đường thủ công cho ticket bị thu hẹp, không thu phạm vi về 0 để làm xanh report. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Ngày đầu cần phạm vi pilot được phê duyệt, người duyệt có thẩm quyền, khả năng dừng đã kiểm chứng và các ngưỡng bắt buộc được ký trước đo. Đề xuất vận hành của TV3 là SLA tiếp nhận 60 phút, cảnh báo sớm 30 phút và mục tiêu dừng 5 phút; hai ngưỡng sau cần nhóm thống nhất, chưa phải kết quả đo. Một người chỉ có năng lực 6 ca/giờ theo mock nên phải kiểm report hàng chờ, công kiểm lại và ROI trước khi nhận là đủ tải. Chỉ kết luận thành công trong phạm vi/bộ thử đã đo; chưa có report hoặc chưa có kênh/người trực thực thì chưa xác nhận đủ điều kiện chạy thật. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ngân sách, số người/công suất, phạm vi, chi phí/ticket, ROI, cảnh báo tải và mức kiểm mẫu phải được đánh giá lại theo lưu lượng từng depot và hành vi kiểm lại thực tế; không nhân nguyên phương án 1 người cho toàn hệ thống. Theo dõi phiên bản chính sách theo ngày hiệu lực và danh sách trường được gửi hãng; ngay trong mock v4 bắt đầu 2026-12-01 đã đổi hạn mức tự động và nguyên nhân quy lỗi. Không nới mục tiêu không ghi oan/không lộ dữ liệu chỉ vì tăng quy mô. Nếu cần đổi tiêu chí thì lập bản cho đợt đánh giá sau, có dữ kiện và ký trước đo; giữ nguyên acceptance_criteria đã ký của lab hiện tại. |

Người soát Bước 2: Lê Viết Khoa — 2A202603737. Đã hoàn thành nội dung rà soát trước đo theo phân công; cả nhóm còn phải đối chiếu bốn câu này với từng ngưỡng/câu tiêu chí do TV1 chốt ở Bước 1. Không chạy eval hoặc trace để viết phần này.

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` ____ · `roi_min` ____ · `queue_stuck_max` ____
- Ngày xem lại tiêu chí: `__________` · Ai dự: `__________` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
