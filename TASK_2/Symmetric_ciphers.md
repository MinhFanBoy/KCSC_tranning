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

1. ECB
+ Các thông tin sẽ được chia thành các khối độc lập, sau đó mã từng khối riêng lẻ với nhau
+ Các Khối được mã độc lập với các khối khác $C_i = E(P_i)$, do vậy nó được dùng để truyền an toàn từng giá trị riêng lẻ
+ Tính chất:
    - Các khối mã như nhau sẽ có bản mã giống nhau (dưới cùng một khóa)
    - Sự phụ thuộc không có nên việc thay đổi sắp xếp các block với nhau thì các bản rõ cũng phải được sắp xếp lại tương ứng
    - Tính lan sai : Khi một hay nhiều bit sai trong một khối đơn lẻ thì nó chỉ ảnh hưởng trong khối đó và không ảnh hưởng tới các khối khác
    - Nó có thể sứ lý nhiều khối song song
   
![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/2532b32e-c5d0-41af-8c30-53ab655430e3)

2. CBC
+ Mẩu tin được chia thành các khối
+ Các block sếp thành dãy trong quá trình mã hóa, giải mã
+ Sử dụng vector IV để bắt đầu quá trình $c_i = e(p_i xor c_i-1), c_-1 = IV$
+ Tính chất :
  - các bản rõ giống nhau cũng chưa chắc cho ra bản mã giống nhau. vì nó còn phụ thuộc vào IV
  - Sự phụ thuộc móc xích: cơ chế mã hóa làm cho bản mã $c_i$ phụ thuộc vào bản mã $c_{i-1}$ nên nếu thay đổi cách sắp xếp các bản sẽ rất khó tấn công. Việc giải mã khối này thì cũng đòi hỏi phải giải đúng khối trước nó nó
  - Tính lan sai: Khi sai một bit trong khối mã thì việc giải, mã tất cả các khối sau nó sẽ bị sai

 
![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/072a2115-17b7-4a53-b4c3-0c4e5c4604dd)



3. CFB
+ Thông tin khi đi vào sẽ dc chia thành các khối
+ các bản rõ dc sắp xếp nên khi giải mã cx yêu cầu thứ tự các bản mã phải đúng.
+ $c_i = p_i \oplus e(k, c_{i-1})$ với $c_{-1} = IV$
+ Tính chất:
  - Các bản rõ giống nhau: giống như CBC
  - Sự phụ thuộc móc xích: giống như CBC
  - Tính lan sai: giống như CBC
  - Không thể thực hiên quá trình giải mã song song vì xử lý của khối sau phụ thuộc vào khối trước

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/f2a5c50f-1fce-44c5-85d6-56955693f674)


    
4. OFB
+ Nhìn chung thì cũng giống các mode trước nhưng khác tý: $c_i = p_1 \oplus e_i(k, c_{i - 1})$ với $c_{-1} = IV$
+ Khi mã hóa của một khối bị sai cũng không ảnh hưởng tới các khối khác
+ Tính bảo mật cao, có thể mã hóa được nhiều khối cùng một lúc nên được tận dụng trong việc truyền tải âm thanh 

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/c261a31d-11d5-4977-b0c2-953a9641f9a2)

  
5. CTR
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

1. Man in the middle.

Man in the middle (MITM) hay còn được gọi là tấn công trung gian được hellman và mackey chỉ ra năm 1977.
Nó là một kiểu tấn công mạng nhằm chặ toàn bộ thông tin của hai bên và mạo danh để có thể làm chủ nhiều thông tin nhạy cảm theo ý của kẻ tấn công. AES, DES và nhiều mã hóa khác được coi là không an toàn trước kiểu tấn công này. Để bảo vệ trước cuộc tấn công này ta cần phải mã hóa thông tin và ký trước khi gửi đồng thời có thể dùng nhiều giao thức bảo mật khác nhằn tăng tính an toàn.

Trên thực tế mã hóa 2DES không thật sự làm tằng số key khóa lên $2 ^ 112$ . Ứng dụng phân tích mật mã (1996), được xuất bản trên Tạp chí Mật mã học, 1999. Họ tuyên bố rằng 2DES cung cấp "chỉ nhiều hơn 17 bit bảo mật" so với DES (con số đó vẫn có thể cao hơn một trăm nghìn lần). Nó vẫn còn rất lớn nên nếu tấn công bằng MITM thì ta sẽ giảm thời tấn công xuống $2 ^ 57$ tức chỉ gấp đôi so với DES.

Giả sử bạn là nhà giải mã có quyền truy cập vào văn bản thuần túy và văn bản được mã hóa. Mục đích của bạn là khôi phục khóa bí mật. Giả sử AAA (bản rõ) -> XXX (Sau lần mã hóa đầu tiên) -> ZZZ (sau lần mã hóa thứ 2).

Bắt đầu với AAA và thử tất cả $2 ^ 56$ cách kết hợp khóa bí mật bằng cách mã hóa AAA. Điều này sẽ cung cấp cho bạn một danh sách lớn các giá trị có thể có cho XXX. Tiếp theo, bạn lấy ZZZ và thử tất cả 256 tổ hợp khóa bí mật bằng cách giải mã ZZZ. Điều này sẽ cung cấp cho bạn một danh sách lớn các giá trị có thể có cho XXX.
Bây giờ hãy thực hiện tra cứu đơn giản giữa hai danh sách để tìm giá trị phù hợp. Ngay khi bạn thấy giá trị XXX phù hợp trong cả hai danh sách, bạn đã tìm ra khóa bí mật. Vì vậy, điều này có nghĩa là với nỗ lực $2 ^ 57$ khóa, bạn đã phá vỡ được mã hóa. EZ attack 😲

2. Padding Oracle
   
**Padding Oracle** là một loại tấn công mật mã khai thác xác thực phần đệm của thông điệp mật mã để giải mã văn bản mã hóa. Cuộc tấn công này chủ yếu liên quan đến **chế độ CBC** hoạt động được sử dụng trong mật mã khối. Trong đó “oracle” (thường là máy chủ) rò rỉ dữ liệu về việc liệu phần đệm của tin nhắn được mã hóa có chính xác hay không. Dữ liệu như vậy có thể cho phép những kẻ tấn công giải mã (và đôi khi mã hóa) tin nhắn thông qua oracle bằng cách sử dụng khóa của oracle mà không cần biết khóa mã hóa.
Việc triển khai tiêu chuẩn của giải mã CBC trong mật mã khối là giải mã tất cả các khối bản mã, xác thực phần đệm, xóa phần đệm PKCS7 và trả về văn bản thuần túy của tin nhắn. Nếu máy chủ trả về lỗi “đệm không hợp lệ” thay vì lỗi chung “giải mã không thành công”, kẻ tấn công có thể sử dụng máy chủ như một oracle đệm để giải mã (và đôi khi mã hóa) message.

<picture>
   <img src="https://i.imgur.com/BW82maM.png">
</picture>

## IV. Write up

### Keyed Permutations

---

**_TASK:_**

What is the mathematical term for a one-to-one correspondence?

---

Trong toán học thuật ngữ một-một làm ta nhớ tới song ánh, khi nó hàm song ánh ta có thể hoàn toàn tìm được hàm nghịch đảo của nó một yêu cầu quan trọng trong việc giải, mã .

> crypto{bijection}

### Resisting Bruteforce

---

**_TASK:_**

What is the name for the best single-key attack against AES?

---

Hỏi google là ta có ngay đáp án. The best publicly known single-key attack on AES is the **biclique attack** which is still the best publicly known single-key attack on AES as of April 2019. The computational complexity of the attack is, and for AES128, AES192 and AES256, respectively. It is the only publicly known single-key attack on AES that attacks the full number of rounds².

> crypto{biclique}

### Structure of AES

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

### Round Keys

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

Hoàn thành nốt hàm này bằng lý thuyết ta vừa học, lấy từng phần tử của trạng thái cộng với phần tử ở vị trí tương ứng của trạng thái là ok 10 điểm.

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
