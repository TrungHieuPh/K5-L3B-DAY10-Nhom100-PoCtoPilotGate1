# Bàn giao thành viên 3 — Lê Viết Khoa, 2A202603737

Ngày 19/11/2026 (GMT+7). Repo: [K5-L3B-DAY10-Nhom100-PoCtoPilotGate1](https://github.com/TrungHieuPh/K5-L3B-DAY10-Nhom100-PoCtoPilotGate1). Nhánh nhóm: [develop](https://github.com/TrungHieuPh/K5-L3B-DAY10-Nhom100-PoCtoPilotGate1/tree/develop); nhánh cá nhân: `khoa/van-hanh-phap-ly`. Đợt cập nhật lấy mốc `7df4754` từ origin/develop. Xem [báo cáo ngắn](bao-cao-thanh-vien-3.md).

## Phần Khoa đã thực hiện

| Phân công | Vị trí | Kết quả |
|---|---|---|
| Câu 1.2 | [Phiếu A, A1](../templates/form-a-criteria.md#a1) | Hai mục tiêu riêng cho kế toán Oanh và trưởng ca Hạnh. |
| Câu 1.4 | [Phiếu A, A2](../templates/form-a-criteria.md#a2) | Đủ 6 ô Telemetry: hành vi, thước đo, dữ liệu không nhãn, công thức, cửa sổ/ngưỡng và điểm mù. Giữ cột Offline của Vĩnh. |
| Bốn câu soát | [Phiếu A, A4](../templates/form-a-criteria.md#a4) | Đối chiếu các bên chịu ảnh hưởng, đánh đổi, ngày 1/ngày 1.000 với đúng ngưỡng đã ký. Giữ phần tiêu chí và ranh giới của người phụ trách. |
| Câu 2.4 | [Phiếu B, B4–B5](../templates/form-b-evaluation-gates.md#b4) | HAZOP một tool: 5 dòng kỹ thuật +3 dòng ngoài kỹ thuật; checklist đủ 9 nhóm, mỗi dòng có PIC thật. Phân biệt code/report do Vĩnh ghi với giả thuyết chưa đo. |
| Câu 2.5 | [Phiếu B, B6](../templates/form-b-evaluation-gates.md#b6) | Hai đóng góp vận hành/pháp lý; chưa thay cuộc thảo luận và lựa chọn cổng của cả nhóm. |
| Câu 2.10 | [Cấu hình](../config/operating_gates.json), [B7.5–B7.6](../templates/form-b-evaluation-gates.md#b7) | Điền operations/legal và đồng bộ runbook 1–3, giờ cao điểm; giữ nguyên business của Hiếu và guards của Vĩnh. |
| Minh chứng cá nhân | [TEAM.md](../TEAM.md#levietkhoa-2a202603737) | Đóng góp, nguồn bằng chứng, khai báo AI; exit ticket cuối buổi còn chờ. |

Checklist được điền đầy đủ nhưng các dòng go-live còn Chưa vì chưa có đủ bằng chứng cho code/config cuối. Không đổi trạng thái thành Xong chỉ vì đã viết quy trình.

## Chữ ký chung đã có — không ký lại

Người đứng tên là **Phan Trung Hiếu — 2A202603763, thay mặt Nhom100**. Lock ghi `2026-11-19T16:07:36`; commit ký `9726c53`. Khoa chỉ ghi lại metadata vào Phiếu A A5, không chạy sign, xóa lock hoặc sửa JSON tiêu chí. `.gitattributes` từ develop giữ CRLF của file tiêu chí đúng bytes đã ký; không chuyển file này sang LF hay lưu tự định dạng.

Ngưỡng giữ nguyên: pass_rate ≥0,97; pass^k ≥0,95; hoàn sai/lỗi hãng oan/PII =0; chi phí ≤6.000đ/ticket; ROI ≥0,6; ca ùn =0. Escalation ≤0,25 là chỉ số nên có. Các dòng PIC ký ở B8/C12 là trách nhiệm quyết định v1/v2 sau này, không phải chữ ký cá nhân bổ sung cho tiêu chí.

## Cấu hình đã điền và giới hạn

- PIC `NV-TUNG`; approver `NV-HANH`; 1 người, tổng công suất 6 ca/giờ; chờ tối đa 60 phút.
- Bật ghi chú quyết định, kiểm mẫu 10%; chặn `customer_note` và `recipient_contact` khi gửi hãng; yêu cầu nguyên nhân ghi lỗi theo chính sách hiệu lực.
- Điều kiện dừng khớp tiêu chí đã ký; mục tiêu quy trình dừng trong 5 phút, cảnh báo sớm khi chờ >30 phút hoặc >3 ca đợi. Chưa kiểm chứng thời gian phản ứng thực.
- `alert_channel` ghi rõ OPS-PILOT-GATE1 là kênh đề xuất; chưa tạo kênh thật/tích hợp gửi tin. `stop_conditions` chỉ là văn bản, không tự dừng.
- Phần business giữ nguyên mốc develop; còn null/cấu hình mặc định, cần Hiếu điền ở B7.4. Không tự coi mode all/100% là phạm vi pilot đã duyệt.

## Việc cần chuyển tiếp

| Người cần nhắc | Việc còn chờ | Vì sao / đầu ra cần gửi |
|---|---|---|
| Ngô Chí Vĩnh | Đo lại base-after sau khi tích hợp config Khoa; gửi report, hàng chờ, chi phí/ROI, regression; sau khi nhóm chốt mới checkpoint và prepared. | Ghi chú/kiểm mẫu làm đổi tải và chi phí. Hai run cũ B0 có trước cấu hình mới; Khoa không chạy eval/trace vì nhóm giao chạy trên máy Vĩnh. |
| Đỗ Thanh Mai | Kiểm lại hai ticket hiểm và test được giao trên bản mới, bổ sung hai câu ranh giới A4 nếu nhóm chưa điền. | Không thay phần việc của Mai; trace phải chứng minh các tầng guard/legal hoạt động cùng nhau. |
| Phan Trung Hiếu | Điền business/B7.4, bản đồ dữ liệu B3, xác nhận kênh/người duyệt dự phòng, rồi cùng nhóm quyết v1. | Cap/phạm vi/ROI business chưa có; không tự đặt thay trưởng nhóm. Cần nguyên bản PRD Lab 9 để đối chiếu độc lập §2, §6. |
| Cả nhóm | Hoàn tất pre-mortem đủ bốn lăng kính và chọn 2–3 cổng, xác nhận quy trình dừng. | B6 hiện mới có đóng góp riêng của Khoa; không nhận là cuộc thảo luận đã diễn ra. |
| Vĩnh và nhóm | Làm rõ/kiểm đường dừng, phê duyệt đúng ticket/khách/approver và lỗi hãng sai tham số còn hở. | Đây là quan sát tĩnh ở B4/B5; không phải lỗi test đã xác nhận và Khoa không sửa code phụ trách của Vĩnh. |
| Cả nhóm sau khi nhận thẻ | Phiếu C, monitor mới, risk register sau sự cố, runbook 4–5, v2, submission và exit ticket. | Chưa có thẻ Sx, report ba mốc, prepared hoặc quyết định v1/v2 đầy đủ. Không bịa kết quả để gom bài. |

`runs/` bị gitignore theo repo. Vĩnh cần giữ journal/report gốc và cuối buổi chạy lệnh collect để đưa đúng bằng chứng vào submission; các số ở B0 là phần nhóm đã ghi, không thay report gốc.

## Tin nhắn gửi nhóm

Khoa đã đồng bộ develop và xong phần được giao: A1 câu 1.2, A2 Telemetry, A4 bốn câu soát; B4 HAZOP, B5 checklist/PIC; operations/legal, runbook 1–3 và giờ cao điểm. Tiêu chí đã do Hiếu ký chung ở 9726c53, không cần ký lại. Nhờ Vĩnh đo lại sau config mới vì đã bật ghi chú/kiểm mẫu 10%; Mai kiểm ticket hiểm và phần ranh giới; Hiếu hoàn thiện business/phạm vi, B3, xác nhận kênh trực và người dự phòng. Chưa có đủ bằng chứng để chốt prepared/v1 hay kết luận pilot thật sẵn sàng.
