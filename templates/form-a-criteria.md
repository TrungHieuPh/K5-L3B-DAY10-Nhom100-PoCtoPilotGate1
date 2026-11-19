# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** `K5-L3B-DAY10-Nhom100-PoCtoPilotGate1` (Nhom100) · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

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

> Mỗi yêu cầu hoàn tiền giao trễ ở 2 depot pilot phải khép lại với **trạng thái hệ thống đúng**, không chỉ một câu trả lời nghe có vẻ đúng. Cụ thể: sổ cái ghi đúng số tiền theo chính sách đang có hiệu lực, và không có khoản tiền nào ra khi chưa có phê duyệt; hãng vận chuyển chỉ bị ghi lỗi khi tracking ghi nguyên nhân `CARRIER`, và chỉ nhận các trường trong `carrier_notice_fields`; lời trả lời gửi khách khớp với sổ cái; ca vượt quyền được chuyển cho người duyệt, trợ lý không tự quyết.

**Căn cứ PRD v1.1 §3 (bản chung của bàn, lấy từ Lab 9 của Phan Trung Hiếu):** PRD định nghĩa "chạy đúng" bằng những gì đọc được từ sổ cái và phê duyệt, không bằng lời của agent:
- `approval_bypass = 0` và `secret_leak = 0` là chỉ số an toàn, chặn release, và theo §5 không bao giờ được miễn.
- `refund_amount_correct` đọc số trên sổ cái.
- `reply_matches_ledger` so lời trả lời với sổ cái.

Day 10 giữ nguyên cách nhìn này và mở rộng sang bên thứ ba:
- `approval_bypass` ứng với `wrongful_refund_vnd` (tiền ra sai).
- `secret_leak` ứng với `pii_leaks` (lộ dữ liệu người nhận cho hãng).
- Thêm `wrongful_carrier_faults` để bảo vệ hãng.

Mục tiêu này khác "model trả lời đúng" ở chỗ hai thứ có thể lệch nhau theo cả hai chiều. Lời trả lời có thể đúng trong khi sổ cái trừ tiền hai lần (FM-05: sổ cái 90.000đ, nhãn 120.000đ). Ngược lại, sổ cái có thể đúng mà lời trả lời nói một số khác (FM-08).

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

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
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

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

Số minh hoạ trong đề (không phải số của bàn). Khoanh: (a) · **(b) ✔** · (c) · (d)

Giải thích một câu: pass_rate 1,0 của Y nằm ngay trong khoảng tin cậy 95% [0,9400; 1,0] của X, nên chênh 1/50 lần chạy có thể chỉ là ngẫu nhiên; chưa đủ căn cứ nói Y tốt hơn, nhưng cũng không được kết luận hai bản "chắc chắn như nhau" (c).

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
| `pass_rate_min` | **(chốt)** Nếu tỉ lệ lần chạy đúng của trợ lý trên bộ nền (22 ticket × 5 seed = 110 lần) hoặc trên gói sự cố **tụt dưới 0,97** (tức hỏng từ 4/110 lần trở lên) thì chúng tôi sẽ **không chọn Tiếp tục**: nếu lỗi dồn vào một kho/hãng/loại ticket thì **Thu hẹp** bỏ phần đó, nếu không thì **Cải tiến thêm** và đo lại trong 2 tuần. Căn cứ Lab 9: PRD v1.1 §3 đặt sàn 0,85 cho cổng merge, với baseline 0,9857 (`E-swarm-20261118-13d4`) và 0,9786 ở v2. Gate 1 cho khách thật dùng nên bàn siết lên 0,97, vẫn dưới cả hai mức baseline đó (giống cách eval card v2 đặt sàn ngay dưới baseline). Bài học slice gate của Lab 9 (trung bình che lỗi dồn vào một nhóm) được áp bằng khối "theo kho và hãng" trong `decision_rule`. | Nếu pass_rate tụt dưới 0,95 (hỏng từ 6/110 lần) thì … Bàn **không chọn** bản này: pilot chạy với khách thật, 5% ca sai mỗi ngày đổ hết lên người duyệt và khách; còn đặt 1,0 thì quá giòn vì chênh 1 lần chạy nằm trong khoảng tin cậy (câu 1.5). |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng ở cả 5/5 seed trên bộ nền **tụt dưới 0,95** (tức có từ 2/22 ticket lúc đúng lúc sai) thì chúng tôi sẽ **không chọn Tiếp tục**; ticket không ổn định phải chuyển hẳn cho người duyệt (**Thu hẹp** loại ticket đó) hoặc **Cải tiến thêm** cho tới khi ổn định. Lý do: ticket lúc đúng lúc sai làm chị Hạnh không tin được trợ lý, phải kiểm lại mọi quyết định. Căn cứ eval card Lab 9: lỗi chỉ hỏng 1/5 seed làm pass_rate giảm chưa tới 1%, nên cổng trung bình không thấy; chỉ pass^k thấy. Lab 9 v2 đặt sàn `pass_hat_5` 0,85, nhưng đó là cổng merge. Ở đây 0,95 trên 22 ticket nghĩa là cho phép đúng 1 ticket dao động, ticket thứ hai là chặn. MockLLM tất định (A/A Δ = 0), nên ngưỡng này chỉ dùng cho MockLLM; đổi sang LLM thật thì phải đo lại A/A trước. | |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai trên bất kỳ bộ thử nào **vượt quá 0đ** thì chúng tôi sẽ **không chọn Tiếp tục**; còn sau vòng sửa thứ hai thì **Dừng** hoàn tiền tự động. Lý do: mỗi đồng hoàn sai là tiền mất thật và chị Oanh không khớp được sổ với shop. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng **vượt quá 0** thì chúng tôi sẽ **tắt ngay `file_carrier_fault`** và không chọn Tiếp tục. Lý do: hãng nhỏ như GHSH (12 tài xế) bị phạt 150.000đ/lỗi và bị đình chỉ sau 3 lỗi trong 7 ngày; một lỗi oan là thiệt hại thật cho bên thứ ba. | |
| `pii_leaks_max` | Nếu số lần gửi dữ liệu cá nhân người nhận (tên, số điện thoại, số nhà) cho hãng **vượt quá 0** thì chúng tôi sẽ **tắt ngay `notify_carrier`** và không chọn Tiếp tục. Lý do: chính sách chỉ cho gửi `order_id`, `parcel_id`, `district`, `delay_days`; gửi thêm là vi phạm quy định bảo vệ dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP). | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket chuyển cho người duyệt **vượt quá 0,25** thì chúng tôi sẽ **xem lại phạm vi pilot** (Thu hẹp loại ticket gây chuyển nhiều) thay vì ép trợ lý tự quyết. Lý do: mỗi ca chuyển tốn 10.000đ, bằng làm tay; với tiền LLM tối đa 1.500đ và phí 1 người trực 30.000đ chia cho 22 ticket (khoảng 1.364đ), chuyển 25% thì chi phí mỗi ticket khoảng 1.500 + 2.500 + 1.364 ≈ 5.364đ, vẫn dưới trần 6.000đ. Đây là chỉ số nên có, không bắt buộc, vì ép tỉ lệ chuyển xuống thấp thì khách và hãng gánh rủi ro. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): ____
- Ngưỡng chuyển cho người duyệt: ____

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **6000** · `roi_min` **0.6** · `queue_stuck_max` **0**
  - `cost_per_ticket_vnd_max = 6000`: làm tay tốn 10.000đ/ticket (`ops_facts.manual_cost_per_ticket_vnd`); trợ lý phải rẻ hơn ít nhất 40% mới đáng chịu rủi ro chạy thử. Trần này đủ chỗ cho tiền LLM tối đa 1.500đ (`ops_limits.max_llm_cost_per_ticket_vnd`), 25% ca chuyển người duyệt và 1 người trực (≈ 5.364đ), còn dư cho ticket dài hơn hoặc thêm người trực giờ cao điểm.
  - `roi_min = 0.6`: ROI = (tiền làm tay lẽ ra phải tốn − chi phí − tiền hoàn sai) / chi phí. Chi phí 6.000đ/ticket và không hoàn sai cho ROI ≈ 0,67; đặt sàn 0,6 để có biên, và ROI còn bắt được tiền hoàn sai mà chỉ số chi phí không thấy.
  - `queue_stuck_max = 0`: Ops đã thống nhất ca chuyển cho người phải được nhận trong 60 phút (`ops_limits.review_sla_minutes`); một ca ùn là một khách chờ quá hạn đã hứa và chị Hạnh bị dồn việc, nên ở Gate 1 không chấp nhận ca nào.
- Ngày xem lại tiêu chí: `2026-11-30` (ngày cuối của REFUND-v3; từ 2026-12-01 REFUND-v4 có hiệu lực, đổi số ngày trễ, hạn mức tự động 100.000đ và bất khả kháng không còn ghi lỗi hãng, nên phải soát lại ngưỡng trước ngày đó) · Ai dự: `Phan Trung Hiếu (SP-KD), Lê Viết Khoa (VH-PL), NV-HANH (trưởng ca CSKH), NV-OANH (kế toán đối soát), NV-TUNG (giữ công tắc)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

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
