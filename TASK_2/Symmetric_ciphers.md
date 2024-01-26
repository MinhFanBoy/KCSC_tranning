Tables of contens
=================
* [I. Tổng quan](#i-tổng-quan-về-mã-khóa-đối-xứng)
  * [1. Mật mã đối xứng là gì](#1-mật-mã-đối-xứng-là-gì-)
  * [2. Một vài thông tin phụ](#2-một-vài-thông-tin-bổ-sung)
* [II. Mã khóa](#ii-các-loại-mã-khóa)

## I. Tổng quan về mã khóa đối xứng

### 1. Mật mã đối xứng là gì ?

Mật mã khóa đối xứng là một loại sơ đồ mã hóa trong đó một khóa giống nhau sẽ vừa được dùng để mã hóa, vừa được dùng để giải mã các tệp tin. Mật mã khóa đối xứng được sử dụng rộng rãi trên nhiều hệ thống máy tính khác nhau nhằm tăng cường bảo mật cho dữ liệu. Một sơ đồ mã hóa đối xứng thường sử dụng một khóa đơn được chia sẻ giữa 2 hoặc nhiều người dùng với nhau. Khóa duy nhất này sẽ được dùng cho cả 2 tác vụ mã hóa và giải mã các văn bản thô (các tin nhắn hoặc mảnh dữ liệu cần được mã hóa). Các thuật toán khóa đối xứng được sử dụng rộng rãi trên nhiều hệ thống máy tính khác nhau nhằm tăng cường bảo mật cho dữ liệu. Mức độ bảo mật của các hệ thống mã hóa đối xứng sẽ phụ thuộc vào độ khó trong việc suy đoán ngẫu nhiên ra khóa đối xứng theo hình thức tấn công brute force. Trong số các sơ đồ mã hóa đối xứng được sử dụng ngày nay thì có 2 loại thông dụng nhất là nền tảng mật mã block và stream.

### 2. Một vài thông tin bổ sung

- Một trong những mã khóa đối xứng phổ biến nhẩt đến hiện tại là AES được công bố năm 2001. Hiên tại nó phổ biến tới mưc một số phần mêm máy tính có phần tệp lệnh riêng để thực hiên AES. !) nó là một mã khóa hay có trong CTF nên cần tập trung vào nó.
- Về cơ bản mã khóa đối xứng được chia làm hai loại cơ bản là Mã khóa khối (block cipher) và Mã khóa dòng (stream cipher)
  - Mã khóa khối là mã khóa mã khóa chia các đoạn bản rõ thành các phần bằng nhau rồi mã khóa lần lượt từng phần (AES, DES, ...) với cùng một key.
  - Mã khóa dòng là mã khóa mà khi mã khóa nó chỉ mã khóa từng bytes hoặc nhiều bytes bằng cách xor nó với một loạt các khóa giả (cũng là AES, DES, ...)
- Mã khóa đối xứng chỉ đặc biệt ở cách nó mã khóa từng khối và mode mã khóa của nó. Đây là điểm khiến nó trở nên khó phá vỡ nếu hông đủ am hiểu về loại mã và mode đó thì việc phá nó gần như là không thể.
- Không hiểu sao các mã khóa cơ bản như ceasar, hill các thứ cũng cùng là mx khóa đối xứng mà không thấy nói đến 🙃

## II. Các loại mã khóa

### 1. DES (data encrpyted standard)

a. Tổng quan về DES

+ Được phát triển bởi NIST năm 1977
+ Đầu vào của DES là các block 64 bit và các đầu ra cũng có 64 bit.
+ Với khóa k có độ dài 56 bit(thực ra ban đầu là 64 bit nhưng trong quá trình mã hóa các bit chia hết cho 8 được lấy để kiểm tra tính chắn lẻ nên còn lại 56)
+ Thuật toán : Đâu tiên trước khi đi vào mã hóa nó sẽ chia thông tin của bản rõ thành các khối 64 bit, từng khối này sẽ lần lượt được đưa vào mã hóa. Mỗi lần mã hóa sẽ có 16 chu trình chính.

b. Chi tiết


Phần tạo khóa:
  
+ Từ khóa 64 bit ban đầu qua phần (Hoán vị PC-1) Permuted choice - 1 loại bỏ các bit ở vị trí chia hết cho 8(từ đó khóa còn lại 56 bit). Tách các bit còn lại làm 2 phần mỗi phần có 28 bỉt là 28 bit đầu và 28 bit cuối(ký hiệu: 28 bit đầu $C_0$, 28 bit cuối $D_0$)
+ Dịch trái: ở các vòng(1, 2, 9, 16) thì ta dich trái 1 bit, các vòng còn lại dịch trái 2 bit.
+ Sau khi dịch vòng trái cho $C_0$ và $D_0$ thì ta sẽ cho vào hoán vị PC-2 . Hoán vị PC-2 về cơ bản là giống hoán vị PC-1 chỉ khác ở sự hoán vị khi các bít 9, 18, 25, 35, 38, 43 bị lược bỏ. Khi này đầu ra của nó sẽ là 18. Lưu lại kết quả sau khi vòng dịch trái rồi gán nó vào $C_1$, $D_1$

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

> Bên trong hàm F()

- Đưa $R_0$ qua hoán vị mở rộng E. Hoán vị mở rộng E là lặp lại hai bit cuối của hàng trước hoặc hàng sau. Mục đích của nó là để tăng số bit lên 48 để $XOR$ với cả $key$ cũng có 48 bits.


![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/78a27ded-a166-4310-b2e0-d2294ea221fb)

- Sau khi $R_0$ xor với $K_0$ thì ta cho nó qua vòng s-box để chuyển nó về lại 32 bit.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/1c374294-e742-4df6-9be9-5e91b665efe1)

- Tiếp tục cho hoán vị PC-1. Sau đó lấy $L_0$ $XOR$ với kết quả vừa có. Rồi gán bằng $R_1$.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/83470541-6257-4c8e-9556-53d87046adba)
> Kết thúc hàm F()

Sau đó ta đặt:

+ $l_{i} = R _ {i - 1}$
+ $R_{i} = L_{i - 1} \oplus F(R_{i - 1}, k_i)$

Lấy phần $L _ {i}, R _ {i}$ tiếp tục thực hàm như trên.

> Sau 16 vòng

Tiếp tục làm như vậy trong 16 vòng. Rồi cho qua hoán vi IP(-1) thì ta sẽ có dc ciphertext.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/60b91532-f0b8-4f12-95b5-27fa87306ef0)


Vậy ta có:
+ $l_{i} = R _ {i - 1}$
+ $R_{i} = L_{i - 1} \oplus F(R_{i - 1}, k_i)$

c. Thông tin thêm

+ DES có hiệu ứng tuyết lở mạnh:
  + với mỗi một bit plaintext bị thay đổi có thể thay đổi ít nhất 34 bit ở ciphertext
  + Mỗi một bit ở Key bị thay đổi khiến ciphertext thay đổi ít nhất 35 bit
+ Với khóa thật sự được dùng trong DES là 56( Thay vì 64 như đầu vào) thì để bruteforce tất cả key (giả sử mỗi lần giải mã mất một giây) thì ta tốn hơn 1000 năm để hoàn thành
+ Hiện tại DES được xem là không an toàn nữa.

### 2. 3DES

a. Tổng quan về 3DES

+ Cũng là DES nhưng được mã hóa nhiều lần với các key khác nhau.
+ Yêu cầu đầu vào và đầu ra cũng giống như DES.
+ Tránh được việc bị bruteforce hay tấn công khác.

b. 3DES

+ 2DES: Sau khi mã hóa lần 1 ta lấy ciphertext đó làm plaintext của lần 2 và mã hóa. Việc giải mã thì ta giải mã với trình tự ngược lại, lấy ciphertext của lần mã hóa thứ 2 mã hóa trước xong tiếp tục mã hóa nó là ta sẽ có thông tin ban đầu.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/01b82852-8e66-4161-bdea-2747d6a66ab5)

+ 3DES: Ta thực hiên như sau: Lấy plaintext mã hóa với $key_1$, giải mã bằng $key_2$ xong rồi tiếp tục mã hóa bằng $key_1$.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/2cf7808c-0bfa-4f6e-8f77-9faeb2029f6b)

c. Thông tin thêm
+ 2DES đã bị phá vỡ bởi các cuộc tấn công vì độ dài khóa quá ngắn.
+ 3DES sử dụng ba khóa DES để mã hóa dữ liệu, mỗi khóa có độ dài 56 bit. 3DES được coi là một phiên bản an toàn hơn của DES và được sử dụng rộng rãi trong các sản phẩm mật mã dân sự. 3DES cũng được sử dụng trong các sản phẩm bảo mật như thẻ tín dụng và các sản phẩm bảo mật thông tin khác

### 3. AES(advanced encryption standard)

a. Tổng quan
+ Được phát triển bởi NIST năm 2001.
+ **AES (Advanced Encryption Standard)** là một thuật toán mã hóa khối đối xứng được sử dụng rộng rãi trong các sản phẩm bảo mật thông tin. Thuật toán này được thiết kế để thay thế cho thuật toán DES (Data Encryption Standard) cũ hơn. AES sử dụng kích thước khối 128 bit và có ba kích thước khóa khác nhau: 128, 192 và 256 bit. AES được coi là một trong những thuật toán mã hóa đối xứng an toàn nhất hiện nay.(Trong bài viết này để dễ ràng hiểu và viết thì mình chỉ viết với AES có kích thước khóa là 128bit)

<picture>
  <img src="https://lilthawg29.files.wordpress.com/2021/06/image-2.png" width="30%" height="30%">
</picture>

+ Với plaintext = 128 bit, key = 128 bit, 192 bit, or 256 bit.
+ Trong khi mã hóa có các khóa mở rộng được sinh ra từ chu trình Rijndeal. Hầu hết các phép toán trong AES đều được thực hiện trên trường hữu hạn của các bytes. Mỗi khối 128 bit dc chia thành 4 cột với mỗi cột 16 bytes xếp thành một ma trận 4x4, còn dược gọi là ma trận trạng thái. Tùy thuộc vào độ dài của khóa mà ta có số lần lặp trong một vòng khác nhau.
+ Gồm hai bước chính là Bước sinh khóa(key generated) và mã hóa(encrypt).

b. Chi tiết

+ Tổng quát cả quá trình mã hóa:

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/ce64b0f9-770b-4e2e-a453-142eea0b2f01)

+ Chi tiết hơn:

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/0348bb66-dd0c-4f9b-9904-1b150f9abf13)

+ Các bước chính:
   + b1 : Khởi tạo plaintext kết hợp với key thông qua addRoundKey
   + b2 : Lặp mã hóa, sử dụng kết quả của bước 1 rồi thông qua 4 hàm chính.
   + b3 : Sau N - 1 vòng, ta cho nó qua 3 hàm (bỏ qua MixColumns) để hoàn thành mã hóa.
  
+ Có N vòng lặp và có N-1 vòng lặp chính(1 -> N - 1).Chủ yếu thực hiện các hàm sau:
   + Subbytes - thay thế các bytes dữ liệu bằng bytes phụ
   + Shift rows - dịch vòng dữ liệu
   + Mix columns - trộn dữu liệu
   + AddRoundKeys - chèn khóa vòng

+ Hàm shift rows: Là phép chuyển đổi các phần tử trong hàng, nó giữ nguyên hàng đầu tiên của ma trận trạng thái. Hàng thứ hai được dịch chuyển qua một cột ở bên trái. Hàng thứ ba được dịch chuyển hai cột, hàng thứ tư được dịch chuyển ba cột.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/7ee52c17-7d56-4723-8db2-0a6c070bd4bf)

 
+ Hàm AddRoundKeys: Hàm này sẽ lấy giá trị của từng phần tử của trạng thái hiện tại(plaintext đang được mã hóa) với từng phần tử tại vị trí tương ứng của key
  
![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/411b7cc5-4ac4-44f7-942c-b65835dcaf39)

+ MixColums : Hàm này thay đổi giá trị của từng cột bằng cách nhân với ma trận. Nó còn được gọi là hàm xtime(hàm nhân x). Mình sẽ giải thích rõ hàm này hơn ở phần cơ sở toán học.
  
<picture>
   <img src="https://lilthawg29.files.wordpress.com/2021/09/image-238.png?w=1024" width="70%" heigth="70%">
</picture>

+ SubBytes - mỗi bytes của state được thay thế bằng 1 bytes khác trên S-box
  - Là quá trình thay thế phi tuyến tính trong đó mỗi bytes được thay thế bằng một bytes khác trong bảng tra
  - S-box là bẳng 16 x 16 chứa hoán vị của 256 ký tự
  - Mỗi bytes trạng thái được thay thế bởi 4 bit trái và cột xác định bởi 4 bit phải, VD: 6D sẽ được thay thế bởi S-box[6][D]
  - Hộp thế s-box được xây dựng trên phép biến đổi phi tuyến (cái này không hiểu lắm)
    
c. Quá trình tạo khóa mở rộng

+ KeyExpansion: Được thực hiện theo hàm quy nạp.
+ Với Rcon = [01, 02, 04, 08, 10, 20, 40, 80, 1b, 36]
+ Với 128 bit key ta có được 16 bytes key, từ đó chia ra làm 4 đoạn key phụ được goi là word được đánh số từ 0 đến 3.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/35e4d27e-75fd-48f8-9007-36a84d1fbdc2)

+ các word sau được tính theo công thức như sau:
  + $word_i = word_{i - 1} \oplus word_{i - 4}$ với mọi $4 \le t < 44$ và i không phải là bội của 4
  + $word_i = g(word_{i - 1}) \oplus word_{i - 4}$ với i là bội của 4

<picture>
   <img src="https://lilthawg29.files.wordpress.com/2021/09/image-244.png?w=1024" width="70%" heigth="70%">
</picture>

+ Hàm g() là hàm thay đổi gồm các bước dịch trái, đổi chỗ với s_box và xor với Rcon:
  + Dịch trái 1 đơn vị các phần tử của word
  + Đổi chỗ với s_box(hàm nãy cũng giống hàn subbytes trong hàm chính)
  + Xor với Rcon[i/4] vì i khi này chi hết cho 4.
    
d. Cơ sở toán học của AES
  + Trong AES các phép toán được thực hiện trên trường hữu hạn GF(2^8)
  + Phép cộng: $A( a_1, a_2, a_3,..), B( b_1, b_2, b_3, ...)$ => $C = A + B = (c_1, c_2, c_3, ...)$ với $c_i = (a_i + b_i) \pmod{2}$
  + Phép nhân: Được thưc hiện trên trường GF(2^8) bằng cách nhân 2 đa thức trong modul bất khả quy m(x).Trong AES $m(x) = x^8 + x^4 + x^3 + x + 1$
  + Phép xtime: (là phép nhân với x) đọc k hiểu j cả hic

e. Độ an toàn
  + tính chất phức tạp của biểu thức s-box trên $GF(2^8)$ cùng với hiệu ứng khuếch tán giúp cho thuật toán không bị phân tích bằng phương pháp nội suy
  + Rcon khác nhau hạn chế tính đối xứng
  + Tính chất phi tuyến tính
  + Các cấu trúc hóa giải mã khác nhau hạn chế được khóa yếu

### 4. PKCS#7

Các loại mở rộng thường được dùng để ký hiệu: $.p7b, .p7s, .p7m, .p7c, .p7r$

Phát triển bởi	RSA Security, 1 March 1998

PKCS#7 là một chuẩn cú pháp cho việc lưu trữ dữ liệu được ký và/hoặc mã hóa. Nó là một trong các chuẩn thuộc họ chuẩn mã hóa khóa công khai (PKCS) được tạo ra bởi RSA Laboratories. Chuẩn này được sử dụng rộng rãi trong các ứng dụng bảo mật thông tin, ví dụ như để lưu trữ chứng chỉ và danh sách thu hồi chứng chỉ (CRL). Phiên bản mới nhất của chuẩn PKCS#7 là 1.5 và có thể được tìm thấy trong RFC 2315. Chuẩn này cho phép đệ quy, thuộc tính, và các loại nội dung khác nhau, chẳng hạn như dữ liệu, dữ liệu đã ký, dữ liệu đã gửi và dữ liệu đã ký và gửi. Nó cũng cho phép lưu trữ chứng chỉ và/hoặc danh sách thu hồi chứng chỉ (CRL)

PKCS#7 được lưu trữ dưới dạng DER hoặc PEM. Dạng PEM cũng giống như DER nhưng được mã hóa Base64 và có đặt ‑‑‑‑‑BEGIN PKCS7‑‑‑‑‑, ‑‑‑‑‑END PKCS7‑‑‑‑‑ để phân biệt.
