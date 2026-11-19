# Báo cáo công việc — Lê Viết Khoa, 2A202603737

Ngày 19/11/2026 (GMT+7). Repo [Nhom100](https://github.com/TrungHieuPh/K5-L3B-DAY10-Nhom100-PoCtoPilotGate1), nhánh `khoa/van-hanh-phap-ly`, tích hợp `origin/develop` mốc `7df4754`. Yêu cầu được đối chiếu với [README](../README.md), [đề bài](../problem-set.md) và [rubric](../RUBRIC.md).

## Đã thực hiện

1. Đồng bộ develop, xử lý xung đột Phiếu A/TEAM; giữ phần Offline của Vĩnh, tiêu chí của Hiếu, code và các kết quả nhóm đã ghi ở Phiếu B.
2. Hoàn thành [Phiếu A](../templates/form-a-criteria.md): mục tiêu Oanh/Hạnh (1.2), đủ cột Telemetry (1.4), bốn câu soát A4; ghi metadata chữ ký chung có sẵn vào A5.
3. Hoàn thiện [Phiếu B](../templates/form-b-evaluation-gates.md): HAZOP 5 dòng kỹ thuật +3 ngoài kỹ thuật, checklist đủ 9 nhóm có PIC thật, hai đóng góp pre-mortem, runbook 1–3 và giờ cao điểm.
4. Điền [operations/legal](../config/operating_gates.json): NV-TUNG là PIC, NV-HANH duyệt, 1 người/6 ca giờ, SLA 60 phút, ghi chú và kiểm mẫu 10%; chặn hai trường dữ liệu gửi hãng và yêu cầu nguyên nhân quy lỗi. Không sửa business của Hiếu.
5. Cập nhật [TEAM](../TEAM.md#levietkhoa-2a202603737), tên tài liệu và [bàn giao](ban-giao-thanh-vien-3.md); dùng link repo mới và nhánh develop.

## Chưa hoàn thành và lý do

| Việc | Lý do / người tiếp tục |
|---|---|
| Chứng minh cấu hình mới đạt chất lượng, chi phí và hàng chờ | Cần Vĩnh đo lại trên máy được nhóm phân công; run cũ không áp dụng nguyên trạng sau khi bật ghi chú/kiểm mẫu. Khoa không chạy eval/trace/grade. |
| Business/phạm vi, B3, ranh giới A4, pre-mortem chung | Thuộc Hiếu, Mai và cả nhóm; không tự chốt thay. Khoa đã làm phần riêng. |
| Kênh cảnh báo thật, người duyệt dự phòng, xác nhận dừng trong 5 phút | Cần nhóm bố trí và kiểm chứng; config chỉ ghi kênh đề xuất, stop_conditions không tự thi hành. |
| Checkpoint/prepared và quyết định v1 | Cần cấu hình chung hoàn tất và report mới; Vĩnh chạy checkpoint, Hiếu/cả nhóm quyết. |
| Phiếu C, runbook 4–5, v2, submission và exit ticket | Chưa nhận thẻ sự cố và chưa có bằng chứng các mốc cần thiết. |
| Đổi tên thư mục dự án local theo tên repo mới | Đã thử nhưng Windows báo Access denied kể cả ngoài sandbox. Giữ thư mục hiện tại; tên hai file báo cáo/bàn giao và link repo đã chuẩn hóa, không ảnh hưởng commit/push. |

## Chữ ký và kiểm tra

Hiếu đã ký thay mặt nhóm ở commit `9726c53`, lock ghi 16:07:36 ngày 19/11/2026. **Không cần từng thành viên ký lại.** Giữ nguyên JSON/lock, quy tắc CRLF và toàn bộ ngưỡng đã ký (chi phí ≤6.000đ, ROI ≥0,6, ca ùn =0, ba chỉ số an toàn =0). Các ô PIC ký v1/v2 còn chờ giai đoạn quyết định.

Kiểm tra đợt này chỉ xác minh chữ ký/hash, cấu trúc phiếu, kiểu cấu hình, tính nhất quán và việc giữ phần của các thành viên; không thay cho kết quả đánh giá của Vĩnh. Checklist go-live vẫn ghi Chưa ở những dòng còn thiếu bằng chứng.
