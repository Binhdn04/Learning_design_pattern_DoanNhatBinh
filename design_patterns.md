# 3 Nhóm Design Pattern Chính

- **Creational (Khởi tạo):** Tập trung vào cách tạo object để tăng sự linh hoạt và khả năng tái sử dụng code.
- **Structural (Cấu trúc):** Tập trung vào cách lắp ghép các object và class. *Ví dụ: Adapter pattern giúp ghép 2 thành phần không tương thích để chúng có thể làm việc được với nhau.*
- **Behavioral (Hành vi):** Tập trung vào cách các object giao tiếp và phân chia trách nhiệm.

---

# 1. Creational Patterns

## Singleton

- **Intent:** Đảm bảo 1 class chỉ có duy nhất 1 instance và cung cấp một điểm truy cập toàn cục đến instance này.
- **Problem:**
  - Cần kiểm soát access tới tài nguyên chung (ví dụ: database connection hoặc 1 file).
  - Cung cấp điểm truy cập chung tới instance đó một cách an toàn hơn so với việc dùng biến toàn cục (global variable có thể bị code khác ghi đè), bằng cách đóng gói logic Singleton trong 1 class.

### Solution
- **Constructor là private:** Không cho phép tạo object trực tiếp (ngăn việc dùng từ khóa `new` từ bên ngoài để tạo instance).
- **Tạo 1 static method để lấy instance (VD: `Static getInstance()`):** Chỉ khởi tạo object trong lần gọi đầu tiên, những lần gọi sau trả lại object đã lưu.
- *Note:* Trong trường hợp multithreading (đa luồng), phải sử dụng **thread lock** (kết hợp double-checked locking) trong hàm `getInstance()` để đảm bảo không tạo ra nhiều instance cùng lúc.

### Pros and Cons 
- **Pros:** 
  - Đảm bảo class chỉ có duy nhất 1 instance.
  - Cung cấp một điểm truy cập toàn cục (global access point) tới instance.
  - Hỗ trợ lazy initialization (chỉ tạo object khi thực sự cần dùng đến).
- **Cons:** 
  - Vi phạm nguyên tắc Single Responsibility (SRP) vì class vừa xử lý logic nghiệp vụ vừa tự quản lý việc tạo instance của nó.
  - Yêu cầu xử lý thread lock phức tạp trong môi trường multi-thread.
  - Khó thực hiện Unit Test (không thể kế thừa do constructor private, không thể override static method).

### Relations with other patterns:
- **Facade:** Đơn giản hóa interface ➔ *"Cho tôi 1 API đơn giản"*
- **Singleton:** Giới hạn instance ➔ *"Chỉ được có 1 object"*
- **Flyweight:** Chia sẻ state ➔ *"Đừng tạo 1 triệu object giống nhau"*

---

## Factory Method

- **Intent:** Cung cấp 1 Interface để tạo object trong superclass, nhưng cho phép subclass thay đổi loại (type) của object sẽ được tạo ra.
- **Problem:** Codebase bị phụ thuộc quá chặt chẽ vào 1 class cụ thể nhất định.
- **Solution:** Thay vì khởi tạo object trực tiếp (bằng hàm constructor thông thường), hãy tạo object thông qua một factory method.

### Applicability
- Khi không biết trước chính xác loại và các thành phần phụ thuộc của object cần làm việc.
- Khi muốn cung cấp cho người dùng khả năng mở rộng thư viện hoặc framework theo ý muốn.
- Khi muốn tái sử dụng các object hiện có để tiết kiệm tài nguyên (thay vì liên tục tạo mới).

### Pros and Cons
- **Pros:** 
  - Tránh sự phụ thuộc chặt chẽ giữa logic tạo object và đối tượng cụ thể được tạo ra.
  - Đảm bảo Single Responsibility: Gom toàn bộ logic tạo object vào một nơi duy nhất.
  - Dễ dàng thêm sản phẩm mới mà không làm hỏng (break) code hiện tại.
- **Cons:** 
  - Làm tăng độ phức tạp của codebase do phải tạo thêm class/interface. Phương pháp này hoạt động tốt nhất khi hệ thống đã có sẵn cấu trúc các lớp con (subclasses).

### Relations with other patterns:
- **Factory Method:** Subclass quyết định tạo ra *cái gì*.
- **Abstract Factory:** Factory quyết định tạo ra cả một *họ (family) các đối tượng* nào.
- **Prototype:** Trả về kết quả bằng cách *copy* một object đã có sẵn.
- **Builder:** Quyết định quy trình xây dựng (build) object *như thế nào*.
- **Template Method:** Subclass quyết định *một bước* cụ thể trong thuật toán.
- **Iterator:** Quyết định cách duyệt qua một *collection* như thế nào.

---

## Abstract Factory

- **Intent:** tạo families các object liên quan đến nhau mà không cần khai báo class cụ thể
- **Problem:** Cần tạo nhiều object liên quan đến nhau, đảm bảo chúng cùng 1 style/family. Hai là thêm family mới ít cần sửa client code.  
- **Solution:** 
                 FurnitureFactory
                /       |        \
          createChair createSofa createTable
              ↓           ↓          ↓
       ┌──────────────────────────────┐
       │       Modern Family          │
       │ Chair + Sofa + Table         │
       └──────────────────────────────┘

### Pros and Cons
- **Pros:** 
  - Tránh sự phụ thuộc chặt chẽ giữa logic tạo object và đối tượng cụ thể được tạo ra.
  - Đảm bảo Single Responsibility: Gom toàn bộ logic tạo object vào một nơi duy nhất.
  - Dễ dàng thêm sản phẩm mới mà không làm hỏng (break) code hiện tại.
- **Cons:** 
  - Làm tăng độ phức tạp của codebase do phải tạo thêm class/interface. Phương pháp này hoạt động tốt nhất khi hệ thống đã có sẵn cấu trúc các lớp con (subclasses).

### Relations with other patterns:
- **Factory Method:** Subclass quyết định tạo ra *cái gì*.
- **Abstract Factory:** Factory quyết định tạo ra cả một *họ (family) các đối tượng* nào.
- **Prototype:** Trả về kết quả bằng cách *copy* một object đã có sẵn.
- **Builder:** Quyết định quy trình xây dựng (build) object *như thế nào*.
- **Template Method:** Subclass quyết định *một bước* cụ thể trong thuật toán.
- **Iterator:** Quyết định cách duyệt qua một *collection* như thế nào.