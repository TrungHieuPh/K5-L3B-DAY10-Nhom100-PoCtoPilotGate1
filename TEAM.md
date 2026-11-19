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

Vai chính: Vận hành và pháp lý. Điền `config/operating_gates.json`, HAZOP, PIC, runbook, dữ liệu cá nhân và chủ trì gom bài nộp.

### Đóng góp cụ thể

Đang thực hiện.

### Bằng chứng

Mã commit, mã lần chạy và dòng trong Phiếu B/C sẽ được bổ sung.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## DoThanhMai-2A202603862

### Phần việc phụ trách

Vai phụ: Kỹ sư cổng hỗ trợ / kiểm thử. Viết behavioral test, dò trace ticket, kiểm regression và hỗ trợ [lab10/monitors.py](lab10/monitors.py).

### Đóng góp cụ thể

- Viết hai ranh giới đầu ra ở Phiếu A, mục A4: giới hạn hoàn tự động theo tracking và chính sách, chuyển người duyệt khi lời khai lệch tracking.
- Phân tích trace `T-002@55` ở Phiếu B, mục B2: hoàn sai 20.000đ, ghi lỗi oan cho VNX và gửi số ngày trễ sai kèm trường `customer_note`.
- Thiết kế hai ca kiểm thử ở Phiếu B, mục B7.3 cho `O-1024/C-08` và `O-1026/C-10`, ghi kỳ vọng và lệnh chạy. Kết quả chờ guard vòng 1 của Vĩnh.
- Dùng Codex để hỗ trợ phân tích trace và soạn nội dung các mục trên.

### Bằng chứng

- [Phiếu A, mục A4](templates/form-a-criteria.md#a4) và [Phiếu B, mục B2](templates/form-b-evaluation-gates.md#b2).
- Trace `T-002@55`, mốc `base`: tracking ở dòng 02, `model_override` ở dòng 03 và các lệnh ghi ở dòng 06–08. Bổ sung trace mốc `after` sau khi kiểm thử cổng vòng 1.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
