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

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/9c503081-35cf-4c3d-be0f-4706976b7ec4)

  
+ Dịch trái: ở các vòng(1, 2, 9, 16) thì ta dich trái 1 bit, các vòng còn lại dịch trái 2 bit.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/63cd27a9-8bad-4ac0-b9b2-aab70b453c7b)

+ Sau khi dịch vòng trái cho $C_0$ và $D_0$ thì ta sẽ cho vào hoán vị PC-2 . Hoán vị PC-2 về cơ bản là giống hoán vị PC-1 chỉ khác ở sự hoán vị khi các bít 9, 18, 25, 35, 38, 43 bị lược bỏ. Khi này đầu ra của nó sẽ là 18. Lưu lại kết quả sau khi vòng dịch trái rồi gán nó vào $C_1$, $D_1$\

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/803f165d-406e-4d1b-aec7-fa44a06b734e)


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

- Sau khi $R_0$ xor với $K_0$ thì ta cho nó qua vòng s-box để chuyển nó về lại 32 bit. Trong S_box ta tách mỗi phần tử của trạng thái thành hai phần gồm hai bit ở đầu và cuối [0][-1] và các bit còn lại [1:-2], đối chiếu nó theo bảng sau đây:

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

### 5. PKCS#7 Padding

PKCS#7 Padding là một chuẩn cú pháp được sử dụng trong các thuật toán mã hóa khối như DES và AES để đảm bảo rằng dữ liệu được mã hóa có độ dài bằng bội số của kích thước khối. Nó được định nghĩa trong RFC 5652 và được sử dụng rộng rãi trong các ứng dụng bảo mật thông tin. Khi dữ liệu cần được mã hóa không phải là bội số của kích thước khối, PKCS#7 Padding sẽ thêm vào các byte padding để đảm bảo rằng dữ liệu có độ dài bằng bội số của kích thước khối. Các byte padding này có giá trị bằng số lượng byte padding được thêm vào. Ví dụ, nếu cần thêm 6 byte padding, mỗi byte đó sẽ có giá trị là 0x06 . Tuy nhiên, nếu độ dài của dữ liệu cần được mã hóa đã là bội số của kích thước khối, PKCS#7 Padding vẫn sẽ thêm vào các byte padding để tránh nhầm lẫn.

Ví dụ: Một loại mã khóa cần có đầu vào là 4 bytes thì ta sẽ buộc phải nhập đủ 4 bytes vào thì nó mới có thể được mã hóa. Trong trường hợp không đủ 4 bytes thì ta có thể dùng PKCS#7 để padding nó như sau: input : \x11\x11\x11, thì sau khi padding ta sẽ có output: \x11\x11\x11\x01. Tương tự với các trường hợp khác.(Nếu input không có gì thì nó sẽ trả về bội số của 4 bytes để tránh nhầm lẫn)

### 6. Modes of block cipher

#### 6.1. ECB
+ Các thông tin sẽ được chia thành các khối độc lập, sau đó mã từng khối riêng lẻ với nhau
+ Các Khối được mã độc lập với các khối khác $C_i = E(P_i)$, do vậy nó được dùng để truyền an toàn từng giá trị riêng lẻ
+ Tính chất:
    - Các khối mã như nhau sẽ có bản mã giống nhau (dưới cùng một khóa)
    - Sự phụ thuộc không có nên việc thay đổi sắp xếp các block với nhau thì các bản rõ cũng phải được sắp xếp lại tương ứng
    - Tính lan sai : Khi một hay nhiều bit sai trong một khối đơn lẻ thì nó chỉ ảnh hưởng trong khối đó và không ảnh hưởng tới các khối khác
    - Nó có thể sứ lý nhiều khối song song
   
![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/2532b32e-c5d0-41af-8c30-53ab655430e3)

#### 6.2. CBC
+ Mẩu tin được chia thành các khối
+ Các block sếp thành dãy trong quá trình mã hóa, giải mã
+ Sử dụng vector IV để bắt đầu quá trình $c_i = e(p_i xor c_i-1), c_-1 = IV$
+ Tính chất :
  - các bản rõ giống nhau cũng chưa chắc cho ra bản mã giống nhau. vì nó còn phụ thuộc vào IV
  - Sự phụ thuộc móc xích: cơ chế mã hóa làm cho bản mã $c_i$ phụ thuộc vào bản mã $c_{i-1}$ nên nếu thay đổi cách sắp xếp các bản sẽ rất khó tấn công. Việc giải mã khối này thì cũng đòi hỏi phải giải đúng khối trước nó nó
  - Tính lan sai: Khi sai một bit trong khối mã thì việc giải, mã tất cả các khối sau nó sẽ bị sai

 
![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/072a2115-17b7-4a53-b4c3-0c4e5c4604dd)



#### 6.3. CFB
+ Thông tin khi đi vào sẽ dc chia thành các khối
+ các bản rõ dc sắp xếp nên khi giải mã cx yêu cầu thứ tự các bản mã phải đúng.
+ $c_i = p_i \oplus e(k, c_{i-1})$ với $c_{-1} = IV$
+ Tính chất:
  - Các bản rõ giống nhau: giống như CBC
  - Sự phụ thuộc móc xích: giống như CBC
  - Tính lan sai: giống như CBC
  - Không thể thực hiên quá trình giải mã song song vì xử lý của khối sau phụ thuộc vào khối trước

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/f2a5c50f-1fce-44c5-85d6-56955693f674)


    
#### 6.4. OFB
+ Nhìn chung thì cũng giống các mode trước nhưng khác tý: $c_i = p_1 \oplus e_i(k, c_{i - 1})$ với $c_{-1} = IV$
+ Khi mã hóa của một khối bị sai cũng không ảnh hưởng tới các khối khác
+ Tính bảo mật cao, có thể mã hóa được nhiều khối cùng một lúc nên được tận dụng trong việc truyền tải âm thanh 

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/c261a31d-11d5-4977-b0c2-953a9641f9a2)

  
#### 6.5. CTR
+ Tạo ra một bộ đếm bằng văn bản gốc, gọi là R(). Mỗi khối nhận được một bộ đếm và một khóa riêng để tạo ra khối đầu ra
+ Khối đầu ra được xor với bản rõ để tạo thành bản mã
  + $c_i = e(R_i) xor p_i$
  + $p_i = e(R_i) xor c_i$
+ Tính chất:
  - Có hiệu quả cao, thực hiện giải mã hoặc mã hóa trên nhiều block
  - có tính an ninh cao không kém các mode khác khi thực hiện đúng cách
  - đơn giản về mặt cấu trúc
  - các biến đếm phải có yêu cầu không được lặp lại để tránh khóa yếu

## III. Attack

### 1. Man in the middle.

Man in the middle (MITM) hay còn được gọi là tấn công trung gian được hellman và mackey chỉ ra năm 1977.
Nó là một kiểu tấn công mạng nhằm chặ toàn bộ thông tin của hai bên và mạo danh để có thể làm chủ nhiều thông tin nhạy cảm theo ý của kẻ tấn công. AES, DES và nhiều mã hóa khác được coi là không an toàn trước kiểu tấn công này. Để bảo vệ trước cuộc tấn công này ta cần phải mã hóa thông tin và ký trước khi gửi đồng thời có thể dùng nhiều giao thức bảo mật khác nhằn tăng tính an toàn.

Trên thực tế mã hóa 2DES không thật sự làm tằng số key khóa lên $2 ^ 112$ . Ứng dụng phân tích mật mã (1996), được xuất bản trên Tạp chí Mật mã học, 1999. Họ tuyên bố rằng 2DES cung cấp "chỉ nhiều hơn 17 bit bảo mật" so với DES (con số đó vẫn có thể cao hơn một trăm nghìn lần). Nó vẫn còn rất lớn nên nếu tấn công bằng MITM thì ta sẽ giảm thời tấn công xuống $2 ^ 57$ tức chỉ gấp đôi so với DES.

Giả sử bạn là nhà giải mã có quyền truy cập vào văn bản thuần túy và văn bản được mã hóa. Mục đích của bạn là khôi phục khóa bí mật. Giả sử AAA (bản rõ) -> XXX (Sau lần mã hóa đầu tiên) -> ZZZ (sau lần mã hóa thứ 2).

Bắt đầu với AAA và thử tất cả $2 ^ 56$ cách kết hợp khóa bí mật bằng cách mã hóa AAA. Điều này sẽ cung cấp cho bạn một danh sách lớn các giá trị có thể có cho XXX. Tiếp theo, bạn lấy ZZZ và thử tất cả 256 tổ hợp khóa bí mật bằng cách giải mã ZZZ. Điều này sẽ cung cấp cho bạn một danh sách lớn các giá trị có thể có cho XXX.
Bây giờ hãy thực hiện tra cứu đơn giản giữa hai danh sách để tìm giá trị phù hợp. Ngay khi bạn thấy giá trị XXX phù hợp trong cả hai danh sách, bạn đã tìm ra khóa bí mật. Vì vậy, điều này có nghĩa là với nỗ lực $2 ^ 57$ khóa, bạn đã phá vỡ được mã hóa. EZ attack 😲

### 2. Padding Oracle
   
**Padding Oracle** là một loại tấn công mật mã khai thác xác thực phần đệm của thông điệp mật mã để giải mã văn bản mã hóa. Cuộc tấn công này chủ yếu liên quan đến **chế độ CBC** hoạt động được sử dụng trong mật mã khối. Trong đó “oracle” (thường là máy chủ) rò rỉ dữ liệu về việc liệu phần đệm của tin nhắn được mã hóa có chính xác hay không. Dữ liệu như vậy có thể cho phép những kẻ tấn công giải mã (và đôi khi mã hóa) tin nhắn thông qua oracle bằng cách sử dụng khóa của oracle mà không cần biết khóa mã hóa.
Việc triển khai tiêu chuẩn của giải mã CBC trong mật mã khối là giải mã tất cả các khối bản mã, xác thực phần đệm, xóa phần đệm PKCS7 và trả về văn bản thuần túy của tin nhắn. Nếu máy chủ trả về lỗi “đệm không hợp lệ” thay vì lỗi chung “giải mã không thành công”, kẻ tấn công có thể sử dụng máy chủ như một oracle đệm để giải mã (và đôi khi mã hóa) message.

<picture>
   <img src="https://i.imgur.com/BW82maM.png">
</picture>

## IV. Write up

### 1. Keyed Permutations

---

**_TASK:_**

What is the mathematical term for a one-to-one correspondence?

---

Trong toán học thuật ngữ một-một làm ta nhớ tới song ánh, khi nó hàm song ánh ta có thể hoàn toàn tìm được hàm nghịch đảo của nó một yêu cầu quan trọng trong việc giải, mã .

> crypto{bijection}

### 2. Resisting Bruteforce

---

**_TASK:_**

What is the name for the best single-key attack against AES?

---

Hỏi google là ta có ngay đáp án. The best publicly known single-key attack on AES is the **biclique attack** which is still the best publicly known single-key attack on AES as of April 2019. The computational complexity of the attack is, and for AES128, AES192 and AES256, respectively. It is the only publicly known single-key attack on AES that attacks the full number of rounds².

> crypto{biclique}

### 3. Structure of AES

---

**_TASK:_**

Included is a bytes2matrix function for converting our initial plaintext block into a state matrix. Write a matrix2bytes function to turn that matrix back into bytes, and submit the resulting plaintext as the flag.

**_File:_**

```py
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    ????

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))
```

---

Bài này ta chỉ phải hoàn thành nốt hàm matrix to bytes nên cũng khá dễ.

```py
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(matrix[0] + matrix[1] + matrix[2] + matrix[3])

```
> crypto{inmatrix}

### 4. Round Keys

---

**_TASK:_**

Complete the add_round_key function, then use the matrix2bytes function to get your next flag.

**_FILE:_**
```py
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    ???


print(add_round_key(state, round_key))


```
---

Hoàn thành nốt hàm này bằng lý thuyết ta vừa học, lấy từng phần tử của trạng thái  với phần tử ở vị trí tương ứng của trạng thái là ok 10 điểm.

```py
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    return [[s[i][j] ^ k[i][j] for j in range(4)] for i in range(4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(matrix[0] + matrix[1] + matrix[2] + matrix[3])


print(matrix2bytes(add_round_key(state, round_key)))

```

> crypto{r0undk3y}

### 5. Confusion through Substitution

---

**_TASK:_**

To make the S-box, the function has been calculated on all input values from 0x00 to 0xff and the outputs put in the lookup table.

Implement sub_bytes, send the state matrix through the inverse S-box and then convert it to bytes to get the flag.

**_File:_**
```py
s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

state = [
    [251, 64, 182, 81],
    [146, 168, 33, 80],
    [199, 159, 195, 24],
    [64, 80, 182, 255],
]


def sub_bytes(s, sbox=s_box):
    ????

print(matrix2bytes(sub_bytes(state, sbox=inv_s_box)))
```
---

Nhớ lại kiến thức vừa đọc, ta có: chỉ cần thay thế giá trị của từng trạng thái vào vị trí tương ứng của xbox.

```py
s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

state = [
    [251, 64, 182, 81],
    [146, 168, 33, 80],
    [199, 159, 195, 24],
    [64, 80, 182, 255],
]


def sub_bytes(s, sbox=s_box):
    return [[sbox[y] for y in x] for x in state]
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(matrix[0] + matrix[1] + matrix[2] + matrix[3])


print(matrix2bytes(sub_bytes(state, sbox=inv_s_box)))
```

> crypto{l1n34rly}

### 6. Diffusion through Permutation

---

**_TASK:_**


We've provided code to perform MixColumns and the forward ShiftRows operation. After implementing inv_shift_rows, take the state, run inv_mix_columns on it, then inv_shift_rows, convert to bytes and you will have your flag.

Challenge files:
  - diffusion.py

**_FILE:_**
```py
def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inv_shift_rows(s):
    ???

# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])


def inv_mix_columns(s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    mix_columns(s)


state = [
    [108, 106, 71, 86],
    [96, 62, 38, 72],
    [42, 184, 92, 209],
    [94, 79, 8, 54],
]
```
---

Bài này ta chỉ cần đổi chỗ giữa các phần tử của ma trận là xong, làm ngược lại. Nhớ cho thêm hàm return(:>)
```py
def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]
    return s

def inv_shift_rows(s):
    s[1][1], s[2][1], s[3][1], s[0][1] = s[0][1], s[1][1], s[2][1], s[3][1]
    s[2][2], s[3][2], s[0][2], s[1][2] = s[0][2], s[1][2], s[2][2], s[3][2]
    s[3][3], s[0][3], s[1][3], s[2][3] = s[0][3], s[1][3], s[2][3], s[3][3]
    return s


# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)
    


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])
    return s


def inv_mix_columns(s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    mix_columns(s)
    return s

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(matrix[0] + matrix[1] + matrix[2] + matrix[3])

state = [
    [108, 106, 71, 86],
    [96, 62, 38, 72],
    [42, 184, 92, 209],
    [94, 79, 8, 54],
]

print(matrix2bytes(inv_shift_rows(inv_mix_columns(state))))
```
> crypto{d1ffUs3R}

### 7. Bringing It All Together

---

**_TASK:_**

We've provided the key expansion code, and ciphertext that's been properly encrypted by AES-128. Copy in all the building blocks you've coded so far, and complete the decrypt function that implements the steps shown in the diagram. The decrypted plaintext is the flag.

Yes, you can cheat on this challenge, but where's the fun in that?

The code used in these exercises has been taken from Bo Zhu's super simple Python AES implementation, so we've reproduced the license here.

**_FILE:_**
```py
N_ROUNDS = 10

key        = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'



def expand_key(master_key):
    """
    Expands and returns a list of key matrices for the given master_key.
    """

    # Round constants https://en.wikipedia.org/wiki/AES_key_schedule#Round_constants
    r_con = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    # Initialize round keys with raw key material.
    key_columns = bytes2matrix(master_key)
    iteration_size = len(master_key) // 4

    # Each iteration has exactly as many columns as the key material.
    i = 1
    while len(key_columns) < (N_ROUNDS + 1) * 4:
        # Copy previous word.
        word = list(key_columns[-1])

        # Perform schedule_core once every "row".
        if len(key_columns) % iteration_size == 0:
            # Circular shift.
            word.append(word.pop(0))
            # Map to S-BOX.
            word = [s_box[b] for b in word]
            # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
            word[0] ^= r_con[i]
            i += 1
        elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
            # Run word through S-box in the fourth iteration when using a
            # 256-bit key.
            word = [s_box[b] for b in word]

        # XOR with equivalent word from previous iteration.
        word = bytes(i^j for i, j in zip(word, key_columns[-iteration_size]))
        key_columns.append(word)

    # Group key words in 4x4 byte matrices.
    return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]


def decrypt(key, ciphertext):
    round_keys = expand_key(key) # Remember to start from the last round key and work backwards through them when decrypting

    # Convert ciphertext to state matrix

    # Initial add round key step

    for i in range(N_ROUNDS - 1, 0, -1):
        pass # Do round

    # Run final round (skips the InvMixColumns step)

    # Convert state matrix to plaintext

    return plaintext


# print(decrypt(key, ciphertext))
```

---

Mình tổng hợp lại các hàm ở bài trước rồi dựa vào thuật toán mã hóa để thực hiện ngược lại. Bài cũng khá dễ dàng vì đã có sẵn các hàm inv từ bài trước.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/3d275a7c-1b2e-4fb2-88e6-04fd36958606)

Từ đó ta có các bước để decrypt như sau:
+ B1: tạo bảng khóa mở rộng
+ B2: thực hiện hàm ADD ROUND KEY, riêng hàm hàm này ta k cần viết lại vì tính chất của phép xor
+ B3: Thực hiện inv_shift, inv_sub, add_key, inv_mix 9 lần
+ B4: Thực hiện nốt 3 vòng inv_shift, inv_sub, add_key là ta sẽ có dc plaintext.


```py
N_ROUNDS = 10

key        = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'

s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)




def sub_bytes(s, sbox=s_box):
    return [[sbox[y] for y in x] for x in s]
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(matrix[0] + matrix[1] + matrix[2] + matrix[3])


def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]
    return s

def inv_shift_rows(s):
    s[1][1], s[2][1], s[3][1], s[0][1] = s[0][1], s[1][1], s[2][1], s[3][1]
    s[2][2], s[3][2], s[0][2], s[1][2] = s[0][2], s[1][2], s[2][2], s[3][2]
    s[3][3], s[0][3], s[1][3], s[2][3] = s[0][3], s[1][3], s[2][3], s[3][3]
    return s


# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)
    


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])
    return s

def add_round_key(s, k):
    return [[s[i][j] ^ k[i][j] for j in range(4)] for i in range(4)]

def inv_mix_columns(s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    mix_columns(s)
    return s

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(matrix[0] + matrix[1] + matrix[2] + matrix[3])


def expand_key(master_key):
    """
    Expands and returns a list of key matrices for the given master_key.
    """

    # Round constants https://en.wikipedia.org/wiki/AES_key_schedule#Round_constants
    r_con = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    # Initialize round keys with raw key material.
    key_columns = bytes2matrix(master_key)
    iteration_size = len(master_key) // 4

    # Each iteration has exactly as many columns as the key material.
    i = 1
    while len(key_columns) < (N_ROUNDS + 1) * 4:
        # Copy previous word.
        word = list(key_columns[-1])

        # Perform schedule_core once every "row".
        if len(key_columns) % iteration_size == 0:
            # Circular shift.
            word.append(word.pop(0))
            # Map to S-BOX.
            word = [s_box[b] for b in word]
            # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
            word[0] ^= r_con[i]
            i += 1
        elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
            # Run word through S-box in the fourth iteration when using a
            # 256-bit key.
            word = [s_box[b] for b in word]

        # XOR with equivalent word from previous iteration.
        word = bytes(i^j for i, j in zip(word, key_columns[-iteration_size]))
        key_columns.append(word)

    # Group key words in 4x4 byte matrices.
    return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]


def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def decrypt(key, ciphertext):
    round_keys = expand_key(key) # Remember to start from the last round key and work backwards through them when decrypting

    # Convert ciphertext to state matrix
    state = bytes2matrix(ciphertext)
    # Initial add round key step
    state = add_round_key(state, round_keys[10])
    
    for i in range(N_ROUNDS - 1, 0, -1):
        state = inv_shift_rows(state)
        state = sub_bytes(state, sbox=inv_s_box)
        state = add_round_key(state, round_keys[i])
        state = inv_mix_columns(state)
        
        

    # Run final round (skips the InvMixColumns step)
    state = inv_shift_rows(state)
    state = sub_bytes(state, sbox=inv_s_box)
    state = add_round_key(state, round_keys[0])
    
    # Convert state matrix to plaintext

    return matrix2bytes(state)



print(decrypt(key, ciphertext))
```
> crypto{MYAES128}

### 8. Modes of Operation Starter

---

**_TASK:_**

The previous set of challenges showed how AES performs a keyed permutation on a block of data. In practice, we need to encrypt messages much longer than a single block. A mode of operation describes how to use a cipher like AES on longer messages.

All modes have serious weaknesses when used incorrectly. The challenges in this category take you to a different section of the website where you can interact with APIs and exploit those weaknesses. Get yourself acquainted with the interface and use it to take your next flag!

Play at https://aes.cryptohack.org/block_cipher_starter

**_FILE:_**

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/f2f774dd-9e99-4d25-853e-795b0356a8fe)

---

Bài này mình chỉ cần lấy gửi yêu cầu và nhân yêu cầu từ web là dc nói chung chỉ cần viết code.

```py


from Crypto.Util.number import *
from requests import *

global url

url = "https://aes.cryptohack.org/block_cipher_starter/"


def decrypt(ciphertext):
    return get(url + "decrypt/" + ciphertext).json()["plaintext"]

def encrypt_flag():
    return get(url + "encrypt_flag").json()["ciphertext"]

print(long_to_bytes(int(decrypt(encrypt_flag()), 16)))
```
> crypto{bl0ck_c1ph3r5_4r3_f457_!}

### 9. Passwords as Keys

---
**_TASK:_**

It is essential that keys in symmetric-key algorithms are random bytes, instead of passwords or other predictable data. The random bytes should be generated using a cryptographically-secure pseudorandom number generator (CSPRNG). If the keys are predictable in any way, then the security level of the cipher is reduced and it may be possible for an attacker who gets access to the ciphertext to decrypt it.

Just because a key looks like it is formed of random bytes, does not mean that it necessarily is. In this case the key has been derived from a simple password using a hashing function, which makes the ciphertext crackable.

For this challenge you may script your HTTP requests to the endpoints, or alternatively attack the ciphertext offline. Good luck!

Play at https://aes.cryptohack.org/passwords_as_keys

**_FILE:_**

```py
from Crypto.Cipher import AES
import hashlib
import random


# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()
FLAG = ?


@chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/passwords_as_keys/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}
```
---

Ta có thể dễ dàng thấy key nằm trong web ở trong file nên ta cần các key có thể rồi brute từng key là ra flag.

```py

from Crypto.Util.number import *
from requests import *
from Crypto.Cipher import AES
import hashlib
import random

global url

url = "https://aes.cryptohack.org/passwords_as_keys/"


def encrypt_flag():
    return get(url + "encrypt_flag").json()["ciphertext"]


with open("pass.txt", "r") as f:
    words = [w.strip() for w in f.readlines()]

enc = encrypt_flag()
enc = bytes.fromhex(enc)

for keyword in words:
    KEY = hashlib.md5(keyword.encode()).digest()
    cipher = AES.new(KEY, AES.MODE_ECB)
    tmp = cipher.decrypt(enc)
    if b"crypto" in tmp:
        print(tmp.decode())
        break
    


```
> crypto{k3y5__r__n07__p455w0rdz?}

### 10. ECB CBC WTF

---

**_TASK:_**

Here you can encrypt in CBC but only decrypt in ECB. That shouldn't be a weakness because they're different modes... right?

Play at https://aes.cryptohack.org/ecbcbcwtf

**_FILE:_**
```py
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/ecbcbcwtf/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/ecbcbcwtf/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}
```
---

Mã hóa bằng CBC và giải mã bằng CBC, trước khi mã hóa nó dc xor với ciphertext trước nó(khối đầu tiên xor với cv), giải mã của ciphertext ta nhận được thì sẽ có các khối như sau:

ciphertext = enc_block_1 +  enc_block_2 + enc_block_3 + enc_block_4 + ...
plaintext = iv $\oplus$ flag_1 +  enc_block_1 $\oplus$ flag_2 ...

từ đó ta dễ thấy nếu lấy ciphertext[:16] $\plus$ plaintext[16:32] thì sẽ có flag, cứ tiếp tục cho tới khi có đủ flag.

```py

from pwn import xor
from requests import *
from Crypto.Util.number import *

def decrypt(flag: str):
    flag_hex = flag
    s = "https://aes.cryptohack.org/ecbcbcwtf/" + "decrypt/" + flag_hex
    tmp = get(s).json()
    return tmp["plaintext"]

def encrypt():
    url = "https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    tmp = get(url).json()
    return int("0x" + tmp["ciphertext"], 16)

def main():
    enc_flag = long_to_bytes(encrypt())
    flag = long_to_bytes(int(decrypt(hex(bytes_to_long(enc_flag))[2:]), 16))
    print(xor(enc_flag[:16], flag[16 : 32]).decode() + xor(enc_flag[16:32], flag[32:]).decode())

if __name__ == "__main__":
    main()

```
