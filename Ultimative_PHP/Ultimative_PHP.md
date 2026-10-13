---
title: Ultimative_PHP

---

**Ultimative_PHP**
- Category: Web
- Rating: Easy
- Flag: `FortID{C0RP_M1GR4T10N_1S_WH3R3_D4T4_G03S_T0_D13_ba76e0c0d8}`

Đây là một thử thách Web mà ứng dụng yêu cầu tất cả dữ liệu xác thực phải được gửi trong cùng 1 request thông qua các query parameter.

Tham số đầu tiên cần được truy vấn là `access.level=administrator`, vì nó chỉ có cơ chế validate dạng thô của dữ liệu truyền vào có chuỗi `access_level=administrator` hay không, nhưng php parser sẽ tự chuyển dấu chấm thành dấu gạch dưới --> Bypass được tham số đầu tiên
![Screenshot 2026-10-10 175957](./Ultimative_PHP_Images/Screenshot%202026-10-10%20175957.png)

Câu hỏi thứ 2 cần 2 tham số là `primary` và `backup` khi so sánh lỏng thì cùng là 1 kiểu, nhưng khi so sánh chặt thì chúng không bằng nhau. Với bài này ta có thể truyền `primary[a]=1&backup[b]=2`
![Screenshot 2026-10-10 180022](./Ultimative_PHP_Images/Screenshot%202026-10-10%20180022.png)

Câu hỏi thứ 3 yêu cầu ta tìm một chuỗi cho parameter `code` mà khi kết hợp cùng với chuỗi `ULTIMATIVE-PHP-2026` để băm bằng MD5 và SHA256 khi so sánh lỏng thì giống nhau, còn so sánh chặt thì khác nhau.
![Screenshot 2026-10-10 181018](./Ultimative_PHP_Images/Screenshot%202026-10-10%20181018.png)

Cụ thể là khi băm thành công sẽ lấy 9 digit đầu tiên, ý tưởng để khi so sánh lỏng bằng nhau là magic hash, còn thực chất nó là các chuỗi khác nhau. Sau khi dùng script `sosanh.py` chạy tự động thì tìm ra được giá trị `59036305`.
![Screenshot 2026-10-10 181655](./Ultimative_PHP_Images/Screenshot%202026-10-10%20181039.png)

:::info
magic hash là chuỗi hash trông giống số dạng lũy thừa khoa học. Ví dụ: 0e1234567
:::

Câu hỏi cuối yêu cầu ta tìm một giá trị `PHP Serialized Object` sau đó encode bằng Base64URL. Object ngoài cùng phải là `MigratedProfile`, thuộc tính displayName là `LegacyTemplate` với template là đường dẫn đến flag.
![Screenshot 2026-10-10 181039](./Ultimative_PHP_Images/Screenshot%202026-10-10%20181259.png)

Khi Server thực hiện `(string)$profile` nó sẽ thực hiện `MigratedProfile::__toString()-->LegacyTemplate::__toString()--> file_get_contents("/flag")`. Cấu trúc logic có thể hiểu như sau:
![Screenshot 2026-10-10 181259](./Ultimative_PHP_Images/Screenshot%202026-10-10%20181655.png)

Ta sẽ test trước bằng script `ques4.py` để đọc file `/etc/passwd` và tìm ra cấp về thư mục root là 5, sau đó chạy script `dapan.py` để lấy được flag.
![Screenshot 2026-10-10 181715](./Ultimative_PHP_Images/Screenshot%202026-10-10%20181707.png)
Sau cùng thu được flag `FortID{C0RP_M1GR4T10N_1S_WH3R3_D4T4_G03S_T0_D13_ba76e0c0d8}`
![Screenshot 2026-10-10 181707](./Ultimative_PHP_Images/Screenshot%202026-10-10%20181715.png)


