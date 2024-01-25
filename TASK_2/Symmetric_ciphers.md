Tables of contens
=================
* [I. Tổng quan](#i-tổng-quan-về-mã-khóa-đối-xứng)
  * [1. Mật mã đối xứng là gì](#1-mật-mã-đối-xứng-là-gì-)
  * [2. Một vài thông tin phụ](#2-một-vài-thông-tin-bổ-xung)
  * [3. Mã khóa](#3-các-loại-mã-khóa)

## I. Tổng quan về mã khóa đối xứng

### 1. Mật mã đối xứng là gì ?

Mật mã khóa đối xứng là một loại sơ đồ mã hóa trong đó một khóa giống nhau sẽ vừa được dùng để mã hóa, vừa được dùng để giải mã các tệp tin. Mật mã khóa đối xứng được sử dụng rộng rãi trên nhiều hệ thống máy tính khác nhau nhằm tăng cường bảo mật cho dữ liệu. Một sơ đồ mã hóa đối xứng thường sử dụng một khóa đơn được chia sẻ giữa 2 hoặc nhiều người dùng với nhau. Khóa duy nhất này sẽ được dùng cho cả 2 tác vụ mã hóa và giải mã các văn bản thô (các tin nhắn hoặc mảnh dữ liệu cần được mã hóa). Các thuật toán khóa đối xứng được sử dụng rộng rãi trên nhiều hệ thống máy tính khác nhau nhằm tăng cường bảo mật cho dữ liệu. Mức độ bảo mật của các hệ thống mã hóa đối xứng sẽ phụ thuộc vào độ khó trong việc suy đoán ngẫu nhiên ra khóa đối xứng theo hình thức tấn công brute force. Trong số các sơ đồ mã hóa đối xứng được sử dụng ngày nay thì có 2 loại thông dụng nhất là nền tảng mật mã block và stream.

### 2. Một vài thông tin bổ xung

- Một trong những mã khóa đối xứng phổ biến nhẩt đến hiện tại là AES được công bố năm 2001. Hiên tại nó phổ biến tới mưc một số phần mêm máy tính có phần tệp lệnh riêng để thực hiên AES. !) nó là một mã khóa hay có trong CTF nên cần tập trung vào nó.
- Về cơ bản mã khóa đối xứng được chia làm hai loại cơ bản là Mã khóa khối (block cipher) và Mã khóa dòng (stream cipher)
  - Mã khóa khối là mã khóa mã khóa chia các đoạn bản rõ thành các phần bằng nhau rồi mã khóa lần lượt từng phần (AES, DES, ...) với cùng một key.
  - Mã khóa dòng là mã khóa mà khi mã khóa nó chỉ mã khóa từng bytes hoặc nhiều bytes bằng cách xor nó với một loạt các khóa giả (cũng là AES, DES, ...)
- Mã khóa đối xứng chỉ đặc biệt ở cách nó mã khóa từng khối và mode mã khóa của nó. Đây là điểm khiến nó trở nên khó phá vỡ nếu hông đủ am hiểu về loại mã và mode đó thì việc phá nó gần như là không thể.
- Không hiểu sao các mã khóa cơ bản như ceasar, hill các thứ cũng cùng là mx khóa đối xứng mà không thấy nói đến 🙃

### 3. Các loại mã khóa

#### 1. DES (data encrpyted standard)

a. Tổng quan về DES

+ Được phát triển bởi NIST năm 1977
+ Đầu vào của DES là các block 64 bit và các đầu ra cũng có 64 bit.
+ Với khóa k có độ dài 56 bit(thực ra ban đầu là 64 bit nhưng trong quá trình mã hóa các bit chia hết cho 8 được lấy để kiểm tra tính chắn lẻ nên còn lại 56)
+ Thuật toán : Đâu tiên trước khi đi vào mã hóa nó sẽ chia thông tin của bản rõ thành các khối 64 bit, từng khối này sẽ lần lượt được đưa vào mã hóa. Mỗi lần mã hóa sẽ có 16 chu trình chính.

b. Chi tiết


Phần tạo khóa:
  
+ Từ khóa 64 bit ban đầu qua phần (Hoán vị PC-1) Permuted choice - 1 loại bỏ các bit ở vị trí chia hết cho 8(từ đó khóa còn lại 56 bit). Tách các bit còn lại làm 2 phần mỗi phần có 28 bỉt là 28 bit đầu và 28 bit cuối(ký hiệu: 28 bit đầu $C_0$, 28 bit cuối $D_0$)
+ Dịch trái: ở các vòng(1, 2, 9, 16) thì ta dich trái 1 bit, các vòng còn lại dịch trái 2 bit.
+ Sau khi dịch vòng trái cho C0 và D0 thì ta sẽ cho vào hoán vị PC-2 . Hoán vị PC-2 về cơ bản là giống hoán vị PC-1 chỉ khác ở sự hoán vị khi các bít 9, 18, 25, 35, 38, 43 bị lược bỏ. Khi này đầu ra của nó sẽ là 18.Lưu lại kết quả sau khi vòng dịch trái rồi gán nó vào C1, D1

Phần input:
+ Cách nhìn trực quan mã hóa DES:

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/35dc8acf-a6c4-4ebe-8e67-d883106ccfcb)
+ Từng vòng của DES:

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/fe33099f-e1ce-4c30-a461-78ede91a279e)


> Bắt đầu
- Cho 64 bit qua hoán vị Sau đó lấy 64 bit chia làm 2 phần $l_0$ và $R_0$.
  
![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/e445d333-af9d-4100-b77b-aba8fb5376d6)

- $R_0$ được đưa vào hàm F.
  
![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/b313f020-d7c2-4957-b188-c12f8b82fff6)

- Đưa $R_0$ qua hoán vị mở rộng E. Hoán vị mở rộng E là lặp lại hai bit cuối của hàng trước hoặc hàng sau. Mục đích của nó là để tăng số bit lên 48 để $XOR$ với cả $key$ cũng có 48 bits.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/78a27ded-a166-4310-b2e0-d2294ea221fb)

- Sau khi $R_0$ xor với $K_0$ thì ta cho nó qua vòng s-box để chuyển nó về lại 32 bit.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/1c374294-e742-4df6-9be9-5e91b665efe1)

- Tiếp tục cho hoán vị PC-1. Sau đó lấy $L_0$ $XOR$ với kết quả vừa có. Rồi gán bằng $R_1$.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/83470541-6257-4c8e-9556-53d87046adba)

> Sau 16 vòng

Tiếp tực làm như vậy trong 16 vòng. Rồi cho qua hoán vi IP(-1) thì ta sẽ có dc ciphertext.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/60b91532-f0b8-4f12-95b5-27fa87306ef0)


Vậy ta có:
+ $l_{i} = R _ {i - 1}$
+ $R_{i} = L_{i - 1} \oplus F(R_{i - 1}, k_i)$


