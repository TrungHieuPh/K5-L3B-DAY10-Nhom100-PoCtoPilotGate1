# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Nhom100`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Nhom100-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S3

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phan Trung Hiếu | 2A202603763 | Sản phẩm và kinh doanh | Có |
|   2 | Ngô Chí Vĩnh | 2A202603724 | Kỹ sư cổng chính |             |
|   3 | Lê Viết Khoa | 2A202603737 | Vận hành và pháp lý |             |
|   4 | Đỗ Thanh Mai | 2A202603862 | Kỹ sư cổng hỗ trợ / kiểm thử |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## PhanTrungHieu-2A202603763

### Phần việc phụ trách

Vai chính: Trưởng nhóm và Sản phẩm và kinh doanh. Chủ trì tiêu chí, Phiếu A, `config/acceptance_criteria.json`, cổng kinh doanh và quyết định v1/v2.

### Đóng góp cụ thể

- Khối 1: viết Phiếu A và `config/acceptance_criteria.json`, ký thay mặt bàn trước lần chạy đầu tiên.
- Khối 2A, câu 2.3 (B3): bản đồ dữ liệu của trợ lý hoàn tiền, nguồn sự thật và bản sao của từng trường then chốt, ví dụ drift REFUND-v3 sang REFUND-v4 ngày 2026-12-01.
- Khối 2B, câu 2.9 (B7.4): điền mục `business` trong `config/operating_gates.json`. Trần hoàn tự động 2.000.000đ/ngày; ngân sách LLM 900đ/ticket (1.500đ trần trừ 600đ các lượt gọi sau bước đọc); `pilot_scope` giữ `all` ở v1; `roi_min` 0,6. Mỗi số kèm lý do từ `ops_limits`, `ops_facts`.
- Xác nhận kênh cảnh báo `OPS-PILOT-GATE1` cho phần vận hành của Khoa.
- Vòng 2 (thẻ S3), trên máy Hiếu:
  - Chạy grade bước 0 và trace `S3-01`, `S3-04`, `S3-20`, `S3-42` ở các mốc base, prepared, after.
  - Tách 35 lỗi oan thành ba nhánh: chính sách hết hạn 15, chưa có nguyên nhân 10, vượt trần 2 lỗi/hãng/ngày 10.
  - Viết cổng 2b trong `lab10/guards.py` (`_gate_carrier_fault`). Từ lỗi tự động thứ 3 của một hãng trong ngày, cổng chặn lệnh ghi lỗi; trần đọc từ `ops_limits`. Hoàn tiền cho khách vẫn đi.
  - Thêm 3 monitor vào `lab10/monitors.py`: `max_auto_strikes_per_carrier_day`, `carrier_strike_cap_held_rate`, `tracking_cause_missing_rate`.
  - Thêm 2 stop_condition "Thẻ S3 · …" vào `config/operating_gates.json`.
- Điền Phiếu C (C0–C12) và quyết định v2 **Tiếp tục**; điền `submission/submission.json`, chạy `check_submission --collect`: ĐỦ THÀNH PHẦN.
- Đã dùng trợ lý AI (Claude Code) ở vòng 1 và vòng 2:
  - Vòng 1: đọc code và dữ liệu mock, đo thử các phương án `business` trên bản sao repo (không ghi vào nhật ký chính thức), soạn nháp B3, B7.4.
  - Vòng 2: đọc trace, viết cổng 2b, 3 monitor, 2 stop_condition, soạn Phiếu C. Mọi con số trong phiếu lấy từ các lần chạy có mã bên dưới.

### Bằng chứng

- Commit ký tiêu chí `9726c53`; [Phiếu A](templates/form-a-criteria.md).
- [Phiếu B, mục B3](templates/form-b-evaluation-gates.md#b3) và [B7.4](templates/form-b-evaluation-gates.md#b7); `config/operating_gates.json` mục `business`.
- [Phiếu C](templates/form-c-incident.md): C4, C6–C9 (fault tree, gate, monitor), C12 (v2).
- Mã lần chạy:

  | Lần chạy | Mã |
  |---|---|
  | Grade bước 0 | `R-S3-grade-20261119-171914-87eab7` |
  | Sau cổng 2b | `R-S3-after-20261119-172131-b40167` |
  | Bộ nền sau cổng 2b | `R-base-after-20261119-172138-b40167` |
  | Bộ nền cấu hình cuối (có `business`) | `R-base-after-20261119-172302-ea4958` |
  | Grade cuối (hash code `ea4958d3eabd`) | `R-S3-grade-20261119-172310-ea4958` |

- Grade cuối: S3 pass 0.25 → 0.8333 → 1.0; lỗi oan 35 → 10 → 0; regression và monitor đều ✅.

### Exit ticket

- **Điều học được:**
  - Cổng vòng 1 đỡ được 25/35 lỗi oan trên thẻ S3 nhưng bỏ sót 10 lỗi. Lý do là mọi cổng chỉ xét từng ticket một, trong khi tác hại nằm ở tổng trong ngày: lỗi thứ 3, thứ 4 của cùng một hãng.
  - Trần 2 lỗi/hãng/ngày đã có sẵn trong `ops_limits`. Bàn cũng đã ghi chú nó ở B7.4 nhưng hoãn lại.
  - Từ nay, khi đặt tiêu chí và cổng, tôi phải hỏi thêm câu "cộng dồn theo ngày, theo hãng thì sao", không chỉ "ticket này đúng chưa".
- **Điều còn chưa chắc:**
  - Ở hệ thật, nguyên nhân trễ (`delay_cause`) có được ghi đúng sự thật và kịp thời không, nhất là ngày bão. Cổng 2 và cổng 2b đều tin hoàn toàn vào trường này.
  - NV-HANH có xác nhận kịp các lỗi bị giữ trong 60 phút không.
  - Mock không đo được hai điều này, nên phải đo trong pilot trước Bước đánh giá 2.

## NgoChiVinh-2A202603724

### Phần việc phụ trách

Vai chính: Kỹ sư cổng. Viết `lab10/guards.py`, chạy eval/trace/gate, thực hiện kiểm thử hành vi và hỗ trợ phân tích phản hồi vòng 2.

### Đóng góp cụ thể

Đang thực hiện.

### Bằng chứng

Mã commit, mã lần chạy, trace và dòng trong Phiếu B/C sẽ được bổ sung.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## LeVietKhoa-2A202603737

### Phần việc phụ trách

Thành viên 3 — Vận hành và pháp lý. Theo phân công Khối 1: Phiếu A câu 1.2, câu 1.4 và A4 Bước 2 (bốn câu soát). Chuẩn bị thêm Phiếu B B4, B5, đóng góp B6, B7.5–B7.6; sau khi nhận thẻ phụ trách phần vận hành/pháp lý ở Phiếu C, đặc biệt C9–C11; phối hợp gom bài nộp.

### Đóng góp cụ thể

Đã đồng bộ nhánh cá nhân với develop, giữ phần Offline/tiêu chí của nhóm và bổ sung mục tiêu của kế toán/trưởng ca, Telemetry, bốn câu soát A4; ghi metadata chữ ký đại diện có sẵn ở A5. Hoàn thiện HAZOP `file_carrier_fault` (5 dòng kỹ thuật, 3 dòng ngoài kỹ thuật), checklist đủ 9 nhóm với PIC có tên, hai đóng góp pre-mortem, runbook 1–3 và giờ cao điểm. Đã điền riêng operations/legal trong operating_gates: NV-TUNG là PIC, NV-HANH duyệt, 1 người/6 ca giờ, SLA 60 phút, ghi chú, kiểm mẫu 10%, chặn hai trường gửi hãng và yêu cầu nguyên nhân ghi lỗi. Giữ nguyên business của Hiếu, code của Vĩnh và tiêu chí đã ký. Chưa coi cấu hình mới là đã đạt trước khi Vĩnh đo lại.

Đã dùng trợ lý AI Codex để đọc yêu cầu, đối chiếu code/dữ kiện mock, hỗ trợ soạn phiếu, cập nhật cấu hình và bàn giao. Ngưỡng phản ứng/kênh cảnh báo cần nhóm xác nhận trước pilot thật; không thay ngưỡng chấp nhận đã ký. Không chạy eval/trace/grade trên máy Khoa.

### Bằng chứng

`templates/form-a-criteria.md` A1 câu 1.2, A2 cột telemetry, A4 Bước 2 và A5; `templates/form-b-evaluation-gates.md` B4–B6, B7.5–B7.6; `config/operating_gates.json` operations/legal. Chuẩn bị ban đầu: `4c435e3`; mốc develop tiếp nhận: `7df4754`; chữ ký chung giữ nguyên: `9726c53`. Báo cáo và bàn giao: [báo cáo TV3](docs/bao-cao-thanh-vien-3.md), [bàn giao TV3](docs/ban-giao-thanh-vien-3.md). Nhánh `khoa/van-hanh-phap-ly`; run_id cũ do Vĩnh ghi ở B0, chưa có run mới cho cấu hình Khoa. Xem log nhánh để truy vết commit tích hợp.

### Exit ticket

Chưa viết kết luận cuối buổi: chờ hoàn thành vòng sự cố và tự ghi một điều học được, một điều còn chưa chắc từ kết quả thực tế.


## DoThanhMai-2A202603862

### Phần việc phụ trách

Vai phụ: Kỹ sư cổng hỗ trợ / kiểm thử. Viết behavioral test, dò trace ticket, kiểm regression và hỗ trợ [lab10/monitors.py](lab10/monitors.py).

### Đóng góp cụ thể

- Viết hai ranh giới đầu ra ở Phiếu A, mục A4: giới hạn hoàn tự động theo tracking và chính sách, chuyển người duyệt khi lời khai lệch tracking.
- Phân tích trace `T-002@55` ở Phiếu B, mục B2: hoàn sai 20.000đ, ghi lỗi oan cho VNX và gửi số ngày trễ sai kèm trường `customer_note`.
- Thiết kế và chạy hai ca kiểm thử ở Phiếu B, mục B7.3 cho `O-1024/C-08` và `O-1026/C-10`. Phát hiện guard ban đầu chưa chuyển người theo A4, bổ sung kiểm tra độ trễ trước lệnh ghi và chạy lại hai ca.
- Dùng Codex để hỗ trợ phân tích trace và soạn nội dung các mục trên.

### Bằng chứng

- [Phiếu A, mục A4](templates/form-a-criteria.md#a4) và [Phiếu B, mục B2](templates/form-b-evaluation-gates.md#b2).
- Trace `T-002@55`, mốc `base`: tracking ở dòng 02, `model_override` ở dòng 03 và các lệnh ghi ở dòng 06–08.
- Guard vòng 1 có kiểm tra `delay_claim_mismatch`, mốc `after`: `T-002@55` đạt theo nhãn, cả hai ca tự viết chuyển người và không phát sinh lệnh ghi. Xem [B7.3](templates/form-b-evaluation-gates.md#b73). Bộ test công khai đạt 13/13.

### Exit ticket

- Điều học được: một ca đạt theo nhãn bộ nền vẫn có thể chưa đáp ứng quy trình chuyển người mà nhóm đặt ra. Cần đọc trạng thái và kiểm các hành động đã ghi.
- Điều còn cần xác nhận: số ca chuyển duyệt khi lời khai lệch tracking có làm hàng chờ vượt SLA trong giờ cao điểm không.
