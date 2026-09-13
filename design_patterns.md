3 nhóm design pattern

- Creational: Cách tạo object để tăng sự linh hoạt, tái sử dụng code

- Structural patterns: Ghép các object. Ví dụ adapter pattern ghép 2 thành phần không tương thích làm việc được với nhau 

- Behavioral: Cách các object giao tiếp, chia trách nhiệm

1. Creational pattern
# Singleton
- Mục đích: Đảm bảo 1 class chỉ có 1 instance và cung cấp điểm truy cập đến instance này
- Vấn đề:
+ Muốn kiểm soát access tới tài nguyên chung như database hoặc 1 file
+ Cung cấp điểm truy cập chung tới instance đó: An toàn hơn global variable (có thể bị code ghi đè) 
, đặt logic singleton trong 1 class

## Solution
- Constructor là private: không cho tạo object trực tiếp, ngăn người khác tạo instance 
- Tạo 1 static method để lấy instance: Static getInstance() → tạo một lần, những lần sau trả lại object đã lưu.
- Note: Trường hợp multithreading phải có thread lock để double check trong get_instance để không tạo nhiều instance cùng lúc

## Pros and cons
- Pros: 1 class - 1 instance, a global access point to the instance, lazy initialization (create the object once) 
- Cons: Violate Single responsibility, need thread lock in multi-thread env, hard to unit test (cannot inheritance due to private constructor, cannot override static method)  

### Compare with other design patterns: 
Facade
   ↓
Đơn giản hóa interface
"Cho tôi 1 API đơn giản"

Singleton
   ↓
Giới hạn instance
"Chỉ được có 1 object"

Flyweight
   ↓
Chia sẻ state
"Đừng tạo 1 triệu object giống nhau"