# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Nhom100`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Nhom100-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

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

Đang thực hiện.

### Bằng chứng

Mã commit, mã lần chạy và dòng trong Phiếu A/B/C sẽ được bổ sung.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

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

Đã đồng bộ nhánh cá nhân với develop, giữ phần Offline/tiêu chí của nhóm và bổ sung mục tiêu của kế toán/trưởng ca, Telemetry, bốn câu soát A4; ghi metadata chữ ký đại diện có sẵn ở A5. Hoàn thiện HAZOP `file_carrier_fault` (5 dòng kỹ thuật, 3 dòng ngoài kỹ thuật), checklist đủ 9 nhóm có PIC, hai đóng góp pre-mortem, runbook 1–3 và giờ cao điểm. Đã điền operations/legal: NV-TUNG là PIC, NV-HANH duyệt, 1 người/6 ca giờ, SLA 60 phút, ghi chú, kiểm mẫu 10%, chặn hai trường gửi hãng và yêu cầu nguyên nhân ghi lỗi. Đợt 2 cập nhật B5, trạng thái B7.5 và dòng cuối B7.6 theo B0/B7.1 mới; phân biệt run đã ghi với run đợt 3 chưa có, không tự tạo số đo hoặc đổi Xong khi chưa đủ bằng chứng. Giữ nguyên business, code, monitors và tiêu chí đã ký.

Đã dùng trợ lý AI Codex để đọc yêu cầu, đối chiếu code/dữ kiện mock, hỗ trợ soạn phiếu, cập nhật cấu hình và bàn giao. Ngưỡng phản ứng/kênh cảnh báo cần nhóm xác nhận trước pilot thật; không thay ngưỡng chấp nhận đã ký. Không chạy eval/trace/grade trên máy Khoa.

### Bằng chứng

`templates/form-a-criteria.md` A1 câu 1.2, A2 cột telemetry, A4 Bước 2 và A5; `templates/form-b-evaluation-gates.md` B4–B6, B7.5–B7.6; `config/operating_gates.json` operations/legal. Chuẩn bị: `4c435e3`; cập nhật đợt 2 theo develop `b2f4a0f`; chữ ký chung: `9726c53`. B0 dòng 4 do Vĩnh ghi: `R-base-after-20261119-164159-01762c`, đã có operations/legal và luật chuyển người; chưa có run sau business/8 monitor mới. Báo cáo: [TV3](docs/bao-cao-thanh-vien-3.md), [rà soát đợt 2](docs/bao-cao-tien-do-dot-2.md), [bàn giao](docs/ban-giao-thanh-vien-3.md). Khoa không chạy eval/trace/grade và chưa có report gốc trên máy. Xem log nhánh để truy vết commit cập nhật.

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
