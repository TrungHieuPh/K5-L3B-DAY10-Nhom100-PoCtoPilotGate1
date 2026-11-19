# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |           |      |     |             |
|   2 |           |      |     |             |
|   3 | Lê Viết Khoa | 2A202603737 | Vận hành và pháp lý |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## LeVietKhoa-2A202603737

### Phần việc phụ trách

Thành viên 3 — Vận hành và pháp lý. Theo phân công Khối 1: Phiếu A câu 1.2, câu 1.4 và A4 Bước 2 (bốn câu soát). Chuẩn bị thêm Phiếu B B4, B5, đóng góp B6, B7.5–B7.6; sau khi nhận thẻ phụ trách phần vận hành/pháp lý ở Phiếu C, đặc biệt C9–C11; phối hợp gom bài nộp.

### Đóng góp cụ thể

Đã chuẩn bị mục tiêu của kế toán và trưởng ca; thiết kế telemetry thông báo gửi hãng ngoài danh sách trường cho phép; trả lời bốn câu soát ở A4 Bước 2 về các bên liên quan, tác hại khi tối ưu chỉ số, điều kiện ngày đầu và việc xem lại khi mở rộng. Đã soạn HAZOP tĩnh trên `file_carrier_fault` (5 dòng kỹ thuật, 3 dòng ngoài kỹ thuật); checklist 9 nhóm việc với trạng thái còn thiếu bằng chứng; hai ý kiến pre-mortem về vận hành và pháp lý; đề xuất runbook 1–3, giờ cao điểm và cấu hình chờ áp dụng đúng mốc. Các đề xuất chưa được coi là kết quả đo hay quyết định chung.

Đã dùng trợ lý AI Codex để đọc yêu cầu, đối chiếu code/dữ kiện mock, hỗ trợ soạn phiếu và danh sách bàn giao. Các ngưỡng đề xuất cần được nhóm giải thích, thống nhất trước khi áp dụng.

### Bằng chứng

`templates/form-a-criteria.md` A1 câu 1.2, A2 cột telemetry, A4 Bước 2; `templates/form-b-evaluation-gates.md` B4–B6, B7.5–B7.6. Tài liệu bàn giao: `docs/thanh-vien-3-ban-giao.md`. Các thay đổi được lưu trên nhánh `khoa/van-hanh-phap-ly`; chưa có run_id đánh giá, bổ sung sau khi ký và đo đúng thứ tự. Xem commit của nhánh để truy vết phần chuẩn bị.

### Exit ticket

Chưa viết kết luận cuối buổi: chờ hoàn thành vòng sự cố và tự ghi một điều học được, một điều còn chưa chắc từ kết quả thực tế.
