# Bàn giao phần việc thành viên 3 — Lê Viết Khoa, 2A202603737

Tài liệu bàn giao lưu trong repo trên nhánh `khoa/van-hanh-phap-ly`, ngày 19/11/2026 (GMT+7). Không phải bằng chứng đã chạy đánh giá hoặc quyết định chung của nhóm. Chỉ ba phiếu A/B/C trong templates được lệnh gom đưa vào submission/docs; tài liệu này dùng để phối hợp công việc.

## Đã làm trực tiếp trong repo

| Vị trí | Nội dung đã chuẩn bị | Trạng thái cần hiểu đúng |
|---|---|---|
| Phiếu A, A1 câu 1.2 | Mục tiêu kế toán Oanh và trưởng ca Hạnh | Có nội dung theo world/code; chờ đối chiếu PRD Lab 9. |
| Phiếu A, A2 câu 1.4 | Telemetry đếm thông báo gửi hãng ngoài allowlist; công thức, dữ liệu, cửa sổ, ngưỡng, điểm mù | Thiết kế trước đo; chưa cài monitor hoặc pipeline cảnh báo. Nhóm phải thống nhất ngưỡng trước ký. |
| Phiếu A, A4 Bước 2 | Trả lời đủ bốn câu soát: các bên liên quan, tác hại tối ưu chỉ số, ngày 1, ngày 1.000 | Đã có nội dung trước đo; chờ cả nhóm đối chiếu các câu/ngưỡng TV1 chốt ở Bước 1. |
| Phiếu B, B4 | HAZOP file_carrier_fault: 5 dòng kỹ thuật và 3 dòng ngoài kỹ thuật | Phân tích tĩnh; chờ trace xác nhận và chọn gate. Không nhận là lỗi đã đo. |
| Phiếu B, B5 | Checklist đủ 9 nhóm: mục kiểm, bằng chứng đang thiếu, phân công dự kiến | Tất cả còn Chưa; PIC TV3 có tên, còn chờ tên TV1/TV2. |
| Phiếu B, B6 | Hai đóng góp vận hành và pháp lý ở thì quá khứ theo pre-mortem | Chờ thảo luận cả nhóm; không thay việc im lặng/đọc vòng tròn và chọn 2–3 gate. |
| Phiếu B, B7.5–B7.6 | Bảng config đề xuất; runbook 1–3; giờ cao điểm; ngưỡng và người xử lý | Bản đề xuất chưa áp dụng, chưa khớp config thực tế; phải chốt và kiểm bằng report trước checkpoint. |
| TEAM.md | Dòng thành viên 3 và mục LeVietKhoa-2A202603737 | Có khai báo dùng AI, công việc đã chuẩn bị. Exit ticket và run_id/commit thực tế còn chờ. |

Không chạy eval/trace/grade, không ký tiêu chí, không checkpoint hoặc tạo kết quả giả. Theo yêu cầu tách nhánh, toàn bộ phần chuẩn bị được lưu bằng commit riêng trên `khoa/van-hanh-phap-ly`; không commit vào main, không push/merge trong đợt này. Các phần A/B của thành viên khác và toàn bộ Phiếu C vẫn chờ người phụ trách/thẻ sự cố. Không đổi logic code, config đang hoạt động hoặc submission.json.

Kiểm tra kỹ thuật phát hiện checkout Windows có CRLF làm 19 file nguồn/dữ liệu/test gốc lệch hash dù nội dung khớp HEAD. Đã khôi phục đúng bytes LF từ HEAD, xác nhận từng SHA-256 khớp MANIFEST; không sửa logic, dữ liệu hoặc manifest. Nội dung bàn giao của nhánh chỉ gồm TEAM, hai phiếu A/B và tài liệu này. Repo đang có core.autocrlf=true, nên TV2 cần tránh lần checkout sau tự chuyển các file gốc về CRLF và kiểm lại hash trước grade.

## Đối chiếu phân công Khối 1 trong ảnh

| Đầu mục giao Khoa | Kết quả rà soát | Còn phụ thuộc |
|---|---|---|
| Câu 1.2, mục tiêu nhìn từ chị Oanh và chị Hạnh — A1 | Đã viết đủ hai mục tiêu riêng, có truy vết/đối soát và năng lực duyệt/SLA. | Đối chiếu PRD Lab 9 khi TV1 cung cấp. |
| Câu 1.4, cột Telemetry — A2 | Đã điền đủ 6 ô: hành vi, thước đo, dữ liệu, cách tính, cửa sổ/ngưỡng và điểm mù. Không dùng nhãn. | Nhóm thống nhất ngưỡng; triển khai/đo ở bước sau, không yêu cầu chạy lúc này. |
| Bước 2, bốn câu soát — A4 | Đã bổ sung đủ 4 câu trả lời, có người thực hiện và các đánh đổi cụ thể. | Đối chiếu các câu/ngưỡng cuối cùng TV1 chốt trước ký. |

Kết luận trong phạm vi được giao: nội dung trước đo của ba đầu mục của Khoa đã được điền; việc chốt chung và đối chiếu PRD/ngưỡng chưa hoàn tất. Cột Offline A2 thuộc Vĩnh, hai câu ranh giới A4 thuộc Mai vẫn để người phụ trách làm. Mốc phút 55 là cả nhóm cùng đọc/chốt JSON; Khoa chưa sửa JSON hoặc chạy eval/trace.

## Những việc còn chờ và người cần nhắc

| Ưu tiên | Cần ai | Việc cần hoàn thành / đầu vào cần gửi | Phần TV3 đang chờ |
|---|---|---|---|
| 1 — trước ký | Thành viên 1 / trưởng nhóm | Chốt tên repo theo quy ước; team khớp tên repo; cung cấp PRD v1.1/eval card Lab 9 đã chọn, họ tên/MSSV các bạn; hoàn thiện Phiếu A và acceptance_criteria. | Đối chiếu mục tiêu, điền tên PIC; thống nhất ngưỡng vận hành/pháp lý. |
| 1 — trước ký | Thành viên 1 và cả nhóm | Thảo luận ngưỡng an toàn 0 sự kiện, hàng chờ tối đa 60 phút, cảnh báo sớm 30 phút, mục tiêu dừng 5 phút; đưa tiêu chí chấp nhận và decision_rule liên quan vào A/config trước ký. 30/5 phút là đề xuất nhóm cần giải thích, không phải giới hạn do dữ liệu quy định. | Chốt runbook; không chỉnh ngưỡng acceptance sau ký. |
| 1 — trước đo | Thành viên 1 | Ký, commit và push tiêu chí một lần; gửi commit/hash/thời điểm. | Sau mốc này TV2 mới đánh giá. TV3 không ký thay. |
| 2 — sau ký | Thành viên 2 | Đo base; gửi run_id/report và trace T-002@55; thông tin hàng chờ, chi phí, ROI, kho/hãng xấu nhất. | Kiểm tính khả thi của staffing/runbook; bổ sung chứng cứ HAZOP/checklist. |
| Trước grade | Thành viên 2 | Giữ LF cho các file gốc khi checkout trên Windows và kiểm SHA-256 theo MANIFEST. Đã khôi phục bản local về đúng bytes HEAD; tránh Git tự đổi lại CRLF. Không sửa code gốc hoặc manifest để bỏ qua kiểm tra. | Giữ điều kiện integrity hợp lệ khi tới vòng sự cố. |
| 2 — khối 2B | Thành viên 1 | Chốt business: trần ngày không vượt Finance 2.000.000đ, ngân sách máy, phạm vi pilot và đường thủ công, ROI; xác nhận kênh OPS-PILOT-GATE1 hoặc tên kênh thật và người dự phòng. | Điền config operations/legal đúng mốc; đồng bộ công thức trần C và phạm vi trong runbook. |
| 2 — khối 2B | Thành viên 2 | Chọn 2–3 gate từ HAZOP/pre-mortem và triển khai; xác nhận ghi lỗi đúng kiện/hãng/chính sách, hoàn tiền/phê duyệt/idempotency; hiện thực đường dừng trong vị trí được phép. | B7.5 chưa thể tuyên bố có dừng thật nếu chưa có guard/công tắc được kiểm chứng. |
| 2 — kiểm thử | Thành viên 4 (hoặc TV2 nếu chưa có TV4) | Viết/đo hai ticket hiểm theo tính chất, gồm payload gửi hãng và ca duyệt; gửi trace/report regression. | Xác nhận bộ lọc legal và kiểm mục quyền hạn/bảo mật. |
| 3 — trước checkpoint | Thành viên 2 + TV1 | Report base-after sau gate; đo phương án staffing khi cần, chi phí/ROI từng kho; chốt operations/legal rồi checkpoint/eval prepared/gate và quyết v1. | Cập nhật checklist, số cuối trong runbook, bằng chứng v1. Không tự coi một người là đủ tải. |
| 4 — sau nhận thẻ | Nhóm + Lab Coach | Số thẻ thực tế và gói incidents/Sx; chạy grade trước sửa, trace ít nhất hai lỗi khác nguồn; cung cấp report ba mốc. | Phiếu C phần riêng, giả định môi trường, HAZOP sự cố, C9–C11 và điều chỉnh config vòng 2. |
| 4 — monitor | Thành viên 2 | Ít nhất một monitor mới không dùng nhãn, có giá trị khác giữa bộ nền và thẻ. Có thể tham khảo thiết kế telemetry A2 nhưng phải chọn theo sự cố và kiểm bằng grade. | Điền bằng chứng C8 và risk register; không dùng escalation_rate có sẵn như monitor mới. |
| 5 — cuối bài | Thành viên 1 + cả nhóm | Quyết v2 có report và decision_rule, ba câu C12, tên/MSSV đầy đủ. | submission.json, collect tới ĐỦ THÀNH PHẦN, TEAM exit ticket và nộp LMS. |

## Cấu hình operations/legal đã soạn, chờ áp dụng đúng mốc

Đây là khối đề xuất để ghép vào `config/operating_gates.json` sau khi đã ký, đo baseline và nhóm thống nhất. Giữ phần business do TV1 phụ trách. Một người/6 ca giờ chỉ là giả thuyết khởi đầu, chưa được chứng minh đáp ứng tải. Tên kênh dưới chưa phải kênh đã tồn tại.

```json
{
  "operations": {
    "pic": "NV-TUNG",
    "approver_id": "NV-HANH",
    "reviewers_on_shift": 1,
    "review_capacity_per_hour": 6,
    "max_queue_wait_minutes": 60,
    "stop_conditions": [
      "Khi thời gian chờ lớn nhất vượt 60 phút hoặc có ca bị ùn, NV-TUNG điều phối hỗ trợ hoặc thu hẹp phạm vi; không đẩy thêm tải vào hàng chờ quá sức.",
      "Khi có hoàn sai được xác nhận hoặc phê duyệt không hợp lệ, NV-TUNG dừng issue_refund trong phạm vi ảnh hưởng và yêu cầu NV-OANH đối soát.",
      "Khi có ghi lỗi hãng oan được xác nhận, NV-TUNG dừng file_carrier_fault trong phạm vi ảnh hưởng; NV-OANH tiếp nhận đối soát với hãng.",
      "Khi có thông báo gửi hãng ngoài danh sách trường cho phép, tạm dừng notify_carrier để xác minh; nếu xác nhận lộ PII, khoanh vùng và xử lý bên bị ảnh hưởng.",
      "Mục tiêu đề xuất: hoàn tất dừng trong 5 phút từ tín hiệu đỏ; stop_conditions chỉ ghi quy trình, cần người thực hiện và đường chặn được kiểm chứng."
    ],
    "alert_channel": "OPS-PILOT-GATE1",
    "decision_note": true,
    "review_sampling_pct": 10
  },
  "legal": {
    "pii_fields_blocked_to_third_party": ["customer_note", "recipient_contact"],
    "carrier_fault_requires_recorded_cause": true
  }
}
```

## Tin nhắn có thể gửi ngay cho nhóm

Mọi người ơi, Khoa (TV3) đã điền A1 câu 1.2, A2 telemetry và đủ 4 câu soát A4 Bước 2 theo phân công Khối 1. Đã chuẩn bị thêm HAZOP B4, checklist B5, hai ý pre-mortem và runbook B7.5–B7.6. Toàn bộ được tách sang nhánh khoa/van-hanh-phap-ly. Nội dung có ghi rõ phần đề xuất/chưa có bằng chứng, chưa sửa config hoặc chạy đánh giá để giữ đúng trình tự lab.

- TV1: gửi mình PRD/eval card Lab 9 đã chọn, tên/MSSV thành viên và tên repo chuẩn; cùng chốt ngưỡng hàng chờ/pháp lý, phạm vi pilot, trần tiền, ROI và kênh cảnh báo. Ký/commit/push tiêu chí xong gửi mã commit trước khi TV2 chạy eval.
- TV2: sau khi tiêu chí đã ký/push, gửi run_id/report base và trace T-002@55. Mình cần hàng chờ, số ca ùn, chi phí/ROI, phân khúc xấu nhất để chốt staffing. Nhờ xem HAZOP B4 để chọn gate; kiểm đúng kiện/hãng/phê duyệt, payload gửi hãng và đường dừng thực tế.
- TV2 lưu ý thêm: bản Windows bị CRLF làm lệch hash gốc; local đã được khôi phục LF đúng HEAD/MANIFEST. Khi checkout lại nhớ giữ LF và kiểm integrity, không sửa manifest để né lỗi.
- TV4: chuẩn bị hai ticket hiểm và kiểm regression; gửi trace xác nhận customer_note/recipient_contact không còn ra hãng khi legal được áp dụng, cùng các kết quả test có mã chạy.
- Cả nhóm: phương án TV3 đề xuất là NV-TUNG làm PIC, NV-HANH duyệt, ban đầu 1 người × 6 ca/giờ, chờ tối đa 60 phút, ghi chú quyết định và kiểm mẫu 10%. Cần kiểm chứng trước checkpoint, chưa coi đây là cấu hình đã chốt. Còn chờ người dự phòng, kênh thật và quyết định phạm vi.

Khi có report/thẻ Sx, mình sẽ hoàn thiện phần vận hành/pháp lý sau sự cố và gom bài. Hiện chưa đủ dữ liệu để chốt v1/v2 hay nộp hoàn chỉnh.

## Checklist kết thúc phần TV3

- [ ] Có PRD Lab 9 và xác nhận mục tiêu A1.
- [ ] Ngưỡng/kênh/người dự phòng được cả nhóm thống nhất trước khi ký khi có liên quan tới acceptance.
- [ ] Các PIC TV1/TV2 có họ tên thật trong B5.
- [ ] Có report baseline, trace và guard, sau đó mới áp dụng config trong khối 2B.
- [ ] Config thực tế, runbook và report khớp nhau; staffing được chứng minh khả thi.
- [ ] Có prepared và v1 trước khi nhận thẻ; không sửa bản chụp vòng 1.
- [ ] Có đúng thẻ, grade trước sửa và monitor mới đã kiểm chứng; hoàn thiện C9–C11.
- [ ] Quyết định v2/ba câu có bằng chứng; điền submission.json, collect và đẩy bản cuối.
- [ ] Hoàn tất TEAM exit ticket, mã bằng chứng và tự nộp link LMS.
