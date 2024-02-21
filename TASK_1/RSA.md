
Tables of contens
=================

* [PART_1: Giới thiệu chung](#part_1-giới-thiệu-chung)
   * [Tổng quan](#1-tổng-quan)
   * [Bài toán phân tích thừa số](#2-factoring-large-intergers)
* [PART_2: Attack](#part_2-attack)
   * [1. Common modulus](#1-common-modulus)
   * [2. Blinding](#2-blinding)
   * [3. Low private exponent](#3-low-private-exponent)
   * [4. Hastad's attack](#4-hastads-attack)
   * [5. Fermat's attack](#5-fermats-attack)
   * [6. Timing attack](#6-timing-attack)
   * [7. random fault](#7-random-fault)
   * [8. PKCS1 attack](#8-PKCS1-attack)
   * [9. Multi-prime attack](#9-Multi-prime-attack)
   * [10. Brute-force CTR leak](#10-Brute-force-attack-on-CRT)
* [Part_3: Write up Crypto hack](#part_3-write-up)
* [Part_4: More write up from task](#part_4-more-write-up)
## PART_1: Giới thiệu chung

### 1. Tổng quan

Mã RSA, được phát minh bởi Rivest, Shamir, Adleman. Sử dụng toán học làm nền tảng, đã nhiều lần bị tấn công nhưng nó vẫn chưa thực hiện được. 

Đặt $n = p * q$ với p, q là hai số nguyên tố lớn có cùng kích thước ($n / 2$ bít). Yêu cầu thấp nhất để được coi là an toàn thì n phải có ít nhất 1024 bit. Lấy e, d sao cho $ed = 1 (\mod{phi} )$,  với $phi = (q - 1)*(p -1)$ trong nhóm $Z_{n}$. Gọi $n$ là module của RSA, e là mã khóa, d là giải mã. Cặp $(N, e)$ là public key, $(N, d)$ là private key.

Một tin nhắn là một số tự nhiên m thuộc nhóm $Z_{n}$. Để mã hóa m, ta cần tính $c = m^e \mod N$. Để giải mã c, ta cần tính $m = c^d \mod N$. Thật vậy:

  + Theo định lý nhỏ Fermat : $c^d = m^d*m^e = m\mod N$

Nếu d được cho việc tính toán m trở nên rất dễ ràng, Khi muốn biết d từ n thì nó trở thành một bài toán khó còn được gọi là trap_door. Khi muốn phá RSA, có $(N, e, C)$, rất khó để tính được $\sqrt[e]{C} \mod N$. Vì nhóm hữu hạn $Z_n$ lớn nên rất khó để tìm $d$ sao cho $M$ đúng. Trong RSA hàm $x \to x^e \mod N$ là một ví dụ cho bẫy sập một chiều. Rễ dàng để tính, nhưng khó để đảo ngược.

### 2. factoring large intergers
 +  Tấn công vào public key đơn giản nhất đó chính là phân tích nhân tử cho n từ đó có thể dễ dàng tìm được phi n thông qua $ed = 1 (\mod phi)$. (Được gọi là tấn công bạo lực :v). Nhưng việc phân tích nhân tử một số lớn là một trong những bài toán khó tốn nhiều thời gian từ đó việc tấn công này trở nên bất khả thi về mặt thời gian.
 +  NgoàiNgoài ra, khi biết $d$ và $e$ thì ta có thể tìm được $n$ từ đó tìm được $(q, p)$.

## PART_2: Attack


### 1. Common modulus

1. External attack

Trong trường hợp một hệ thống có chung một N, và mỗi người dùng có một cặp $(e_i, d_i)$ khác nhau. Mặt khác, thông thường $gcd(e_a, e_b) = 1$, chọn u, v sao cho $e_a * u + e_b * v = 1$(có nhiều cách tính, đơn giản nhất là dùng Euclid mở rộng)
$$m ^ {e_a} \equiv c_a \pmod{n} \quad \text{and} \quad m ^ {e_b} \equiv c_b \pmod{n}$$
$$c_a ^ {v} \equiv m ^ {e_a * v} \pmod{n}$$
$$c_b ^ {u} \equiv m ^ {e_b * u} \pmod{n}$$
$$\to c_a ^ {v} * c_b ^{u} \equiv m ^ {e_a * u + e_b * v} = m \pmod{n}$$

2. Internal attack

Để tránh tạo ra một modulo nhiều lần cho mọi người thì việc tạo ra một mod cho nhiều người dùng thoạt nhìn thì có thể vẫn an toàn(dùng chung một $N$ cho nhiều người dùng và có các hệ số $e, d$ khác nhau).

Nếu chúng ta biết $e_a, d_a$ thì thì ta hoàn toàn tìm ra dc $q, p$ của $N$. Từ đó với $e_b$ của một người bất kỳ nào đó thì ta sẽ tính ra dc $d_b$ đó và từ đó có thể dễ dàng mã hóa được $c_b$.

Giả sử: $e_a, d_a,N$ đã biết lúc đó ta có:
Tồn tại $k$ sao cho $e_a * d_a = 1 + k * phi$
$$phi = (e_a * d_a - 1)/k \text{   } \forall phi \in N^*$$
Từ đó ta dễ dàng tìm được phi. Và ta cũng có $phi = (p - 1) * (q - 1) \to phi = N - q - p + 1$

Xét phương trình $(x - q) * (x - p) == 0$, dễ thấy pt có hai nghiệm phân biệt là $p, q$. Phương trình tương đương $x^2 - (p + q) * x + p * q = 0$. Kết hợp với phi đã tính ở trên, ta có: $$x^2 - (N - phi + 1) * x + N = 0$$
Từ đó dễ dàng tìm được $p, q$ , để chắc chắn có thể thêm điều kiện $q, p$ là số nguyên tố. Với $phi, e_b$ ta hoàn toàn có thể tính ra $d_b$ rồi từ đó mã hóa tin nhắn.


### 2. Blinding
   Với $(N, e)$ là khóa chung, $(N, d)$ là khóa chung.
  Với M là tin nhắn chưa được mã hóa, chọn một số r thuộc $Z_n^*$ lấy $M' = r * M$. GỬi M' đi ta nhận được $c_1 = M' ^ d = (M * r) ^ d \pmod{n}$. Gửi r đi ta nhận được $c_2 = r ^ d \pmod{n}$.Từ đó :
  $$c_1 / c_2 = (M * r) ^ d / r ^ d = (r / r * M) ^ d = M ^ d \pmod(n)$$
  Từ đó tùy thuộc vào yêu cầu của bài toán mà ta sẽ tính toán thêm. (Chú ý: Kỹ thuật này hay được sử dụng để ký các đoạn mã hóa.)

### 3. Low private exponent

1. Weinner attack
   Khi $e$ quá nhỏ thì dẫn tới việc d bị quá lớn từ đó dẫn tới việc giải mã bị tốn nhiều thời gian. Để không bị tốn nhiều thời gian thì cho $e$ lớn, dẫn tới việc $d$ nhỏ hơn và giảm thời gian mã hóa. Nhưng nếu $d$ quá nhỏ sẽ dẫn tới trường hợp khóa yếu từ đó dễ bị tấn công.Khi $d < \sqrt[4]{N} / 3,  q < p < 2 * q$, ta có thể tấn công như sau:
   + $e * d = 1 (\mod phi)$ $\to$ $ed = 1 + k*phi$ $\to$ $e/phi - k/d = 1/(d * phi)$ vì $1/(d * phi)$ rất nhỏ nên từ đó ta có thể suy ra $e/phi = k/d$
   + $phi = (q - 1)*(p - 1)$ $\to$ $phi = N - q - p +1 \to p + q -1 = 1/3 (n^(1/2))$ nên $|N - phi| = 1/3 (n^{1/2})$
   + $e / N - k / d = (e * d - k * N)/(N * d)$ $=$ $(e * d - k * phi + k * N + k * phi) / (N * d)$ $<$ $(N^2)/2$



   Từ đó sử dụng tính chất của phân số, ta có thể dễ dàng tính được $k/d$ (:v không hiểu j). Từ đó ta tìm được $d$. từ $d$ và $e$ ta có thể dễ dàng tính $phi$.

   Để tránh trường hợp bị tấn công wiener đã đưa ra 2 cách bảo vệ như sau:
      + đặt $e' = e + k * phi$, sao cho $e' > n^{1.5}$ khi đó ta không thể tấn công với cả $d$ rất nhỏ.
      + Sử dụng d lớn và giải mã bằng CRT. Tìm $d_p, d_q$ rồi dùng CRT để tính m dựa vào hệ $m_p \equiv c^{d_p} \pmod{p}$ và $m_q \equiv c^{d_q} \pmod{q}$
 
$$
\begin{cases}
  m = m_p \pmod{p}\\
  m = m_q \pmod{q}
\end{cases}
$$

2. e attack

Khi chọn e quá nhỏ (thường là dạng $2 ^ k + 1$ để giảm thời gian tính) như 3, 5 thì với n quá lớn cũng có thể khiến nó dễ bị tấn công. Cụ thể, khi $m ^ e < n$ từ đó nó kiển phép mod trở nên vô dụng, từ đó ta có thể dễ dàng tính lại bản mã chỉ bằng phép căn quen thuộc.
$$m = \sqrt[e]{c} $$
Còn nếu với n quá nhỏ thì sẽ dẫn tới việc có thể factor ra được p và q từ đó dẫn tới việc nó dễ bị phá.

Vậy nên khi đó ta có thể dùng pad(có nhiều cách pad những dễ nhất thì cứ thêm thông tin rác vào bản rõ) để tăng thêm độ dài bản mã từ đó khiến cho nó đảm bảo an toàn.

### 4. Hastad's attack
Để thực hiện cuộc tấn công này cần có ít nhất 3 tín nhắn được mã hóa có nội dung giống nhau và có chung e và tất cả các N lần lượt từng đôi một nguyên tố cùng nhau. Từ đó ta có:
   
$$
\begin{cases}
  c_1 = M^3 \pmod{n_1}\\
  c_2 = M^3 \pmod{n_2}\\
  c_3 = M^3 \pmod{n_3}
\end{cases}
$$

  Khi đó sử dụng CRT với hệ trên ta sẽ có được $M^3$. Lấy $\sqrt[3]{X}$ là ta có được M.
  
### 5. Fermat's attack

1. Fermat attack
Trong RSA, $q, p$ nên có chung độ dài để có thể tạo nên một khóa mạnh mẽ, nhưng nếu $q, p$ quá gần nhau lại dẫn dến trường hợp khóa yếu dễ bị tấn công.
Giả sử: $N = (a - b) * (a + b) = a^2 - b^2 \quad \forall a, b \in Z^*$
$$b^2 = a^2 - N$$
$$b = \sqrt{a^2 - N}$$

Với $a = \sqrt{N}, b = a^2 - n$ thử lần lượt với mọi $x > a$ sao cho thỏa mãn hệ.Với cách brute force như vậy nên cách tấn công này chỉ áp dụng với các số q và p gần nhau

2. Random attack

Khi ta biết $q, p$ gần nhau thì ngoài cách trên ta có thể tính theo cách sau nếu p rất gần q. Rõ ràng khi đó $$n = p * q \approx p ^ 2 \forall p < q < n$$ nên từ đó ta có thể tính $p \approx \sqrt[2]{n}$. Từ đó ta có thể dễ dàng tính ra $q = n / p$ hoặc sử dụng hàm nextPrime(p) trong python. Nhưng cách này hầu như không dùng dc nhiều bời vì nó yêu cầu p và q phải đủ gần nhau và n cũng không quá lớn để khi sử dụng hàm khai căn thì nó có thể tính xấp xỉ ra q or p. Cách này hầu như không có tác dụng trong thực tế.

### 6. Timing attack
Đây là kiểu tấn công đươn giản và rất không hiệu quả nên không được sử dụng trong thực tế.

Viết d dưới dạng nhị phân ta có: $d = d_0d_1...d_n$ nên $d = \displaystyle\sum_{i=0}^{n} 2^i * d_i$.
   Từ đó, đặt $$z = M, c = 1, i = 0, ..., n$$

$$
\begin{cases}
  c = c * z \pmod{N} & \text{if } d_i = 1\\
  z = z ^ 2 \pmod{N} & \text{else} \\
  C = M ^ \pmod{N} & \text{when end}
\end{cases}
$$

Vì d là số lẻ nên $d_0$ luôn bằng $1$, Ở lần lặp tiếp theo vì có sự khác biệt giữa thời gian thực hiện phép tính nên ta có thể xác định lần lượt các $d_i$ tiếp theo. Cứ tiếp tục như vậy để khôi phục $d$. Lưu ý khi số $e$ nhỏ dược sử dụng ta chỉ cần khôi phục $1/4$ số bít của $d$.

### 7. random fault
Trong RSA, việc giải mã có thể sử dụng CRT để giảm thời gian chạy. Thay vì hoạt động trên modulus $N$ thì ta chỉ hoạt động trên $q, p$ từ đó giúp giảm thời gian.

   + $c_p = M^{d_p} \pmod{p}$ và $c_q = M^{d_q} \pmod{q}$
   + với $d_p = d \pmod{p - 1}, d_q = d \pmod{q - 1}$
   + $c = a * c_p + b * c_q \pmod{N}$

Trong một vài trường hợp có thể sảy ra lỗi như sau: $${c_q} ^ e = M \pmod{p}$$ $${c_p} ^ e \neq M \pmod{p}$$.  $$\to \gcd(N, {c_p} ^ e) = p$$. Để kiểu tấn công này hoạt động, ta cần phải biết $M$. Nên yêu cầu $M$ phải là văn bản thuần không được pad.

### 8. PKCS1 attack

. Tấn công này là một tấn công ciphertext được chọn trên mã hóa RSA khai thác lỗ hổng của gói đệm PKCS#1 v1.5 1. Tấn công hoạt động bằng cách khai thác việc gói đệm là xác định và kẻ tấn công có thể sử dụng một bộ phận để xác định liệu một ciphertext cụ thể có được đệm đúng hay không. Tấn công có thể được sử dụng để khôi phục các plaintext được mã hóa bằng RSA với đệm PKCS#1 v1.5. Tấn công đã được sử dụng để phá vỡ mã hóa SSL/TLS.

Với $N$ có $n$ bits RSA và tin nhắn mã hóa có $m$ bits mà $m < n$ thì trước khi được mã hóa tin nhắn thường được pad thêm sao cho $m' = n$. Tiêu chuẩn thường dược sử dụng để pad là PKCS1, nó có dạng:
    $$02 + random + 00 + M$$

Có một máy chủ SSL, máy chủ này sẽ gửi các thông báo lỗi riêng biệt tùy thuộc vào việc có tìm thấy phần đệm PKCS#1 thích hợp hay không. Ngoài ra, hai trường hợp có thể được phân biệt thông qua một số rò rỉ thông tin khác (ví dụ: máy chủ mất nhiều thời gian hơn để phản hồi nếu phần đệm chính xác). Bây giờ ta lấy được bản mã c và biết $c = m ^ e \pmod{n}$ với c là bản mã, m là bản rõ, (e, n) là cặp khóa publickey. Bây giừo ta muốn đọc được m, hoặc ít nhất cx muốn biết nó chứa thông tin gì.

Bây giờ ta bắt đầu nhiều kết nối đến máy chủ. Đối với mỗi kết nối, kẻ tấn công tạo ra một giá trị s và gửi nó tới mấy chủ dưới dạng $c' = (s * c)*e \pmod{n}$ máy chủ sẽ giải nó và gửi về cho ta $c' ^ d = s * c \pmod{n}$
. Hầu hết thời gian, giá trị $m * s$ sẽ không được đệm đúng cách (nó sẽ không bắt đầu bằng 0x00 0x02 hoặc sẽ không chứa thêm 0x00). Tuy nhiên, với xác suất thấp nhưng không đáng kể (khoảng 30000 đến 130000 lần thử một lần), ta có thể có $m * s$. Khi đó giá trị trông có vẻ đệm. Nếu đúng như vậy thì máy chủ sẽ thông báo. Với giá trị này s (biết điều đó vì anh ta đã chọn nó), sau đó $m * s \pmod{n}$ nằm trong một phạm vi cụ thể (phạm vi số nguyên bắt đầu bằng 0x00 0x02 khi được mã hóa theo byte bằng quy ước big-endian).

Phần còn lại của cuộc tấn công đang được thử lại với các giá trị ngẫu nhiên được lựa chọn cẩn thận. Mỗi lần máy chủ phản hồi với "đó là phần đệm PKCS#1 thích hợp", điều này sẽ cung cấp một số thông tin giúp kẻ tấn công thu hẹp dự đoán của hắn về m. Sau vài triệu kết nối, ta có thể xác định chính xác m
    
### 9. Multi-prime attack

Trong RSA, ta thường  thực hiện các phép toán trên trường $Z_n$ với n = p * q, vậy nếu n là tích của nhiều số nguyên tố thì sao ?

Có $n = \prod{prime}$ nên từ đó ta dễ có $phi = \prod {prime - 1}$. Vậy ta cũng có thể dễ dàng tính $d = e ^ {-1} \pmod{phi}$ và giải mã như bình thường.

Vậy tại sao ta lại sử dụng nhiều số nguyên tố để tạo ra n thay vì chỉ hai số như bình thường ?

Hmmm có lẽ thay vì việc muốn tạo ra một n có k key_size thì phải tìm ra hai số nguyên tố có ít nhất $\sqrt{k}$ key_size tốn nhiều thời gian và đảm bảo nó phải chưa đc factor thì ta chỉ cần tìm nhiều số nguyên tố nhỏ hơn và tỷ lệ bị factor của nó cx thấp. Còn về tính an toàn, việc phân tích một số là tích của nhiều số nguyên tố cũng khó không khác gì bài toán kia, ít nhất với máy tính bây giờ thời gian để tính của nó vẫn không khả thi. Ngoài ra, khi sử dụng n là tích của nhiều số nguyên tố, ta có thể sử dụng CRT(chinese remain theorem ) để tăng tốc độ tính toán lên nhiều lần. Nên từ đó việc sử dụng nhiều số nguyên để tạo ra n là hoàn toàn khả thi và có thể xuất hiện trong các cuộc thi CTF. 


              
### 10. Brute force attack on CRT

Để sử CRT trong quá trình mã hóa ta phải tính:
$$d_p = e ^ {-1} \pmod{p - 1}$$
$$d_q = e ^ {-1} \pmod{q - 1}$$

Vậy giả sử bằng cách nào đó ta có được $d_p$ hoặc $d_q$ thì ta sẽ làm gì? Nếu số e được chọn đủ tệ để tạo ra các $d_p, d_q$ đủ nhỏ để brute thì ta sẽ làm gì ?


Chọn một số ngẫu nhiên $m \quad \forall m < n$


Dễ có:

$$d_q * e = 1 \pmod{q - 1}$$

$$d_q * e = 1 + k * (q - 1) \quad \forall k \in R$$

$$m ^ {e * d_q} \equiv m ^ {1 + k (q - 1)}\pmod{p}$$

$$m ^ {e * d_q}= m \pmod{n} \text{(Theo định lý nhỏ của fermat)}$$

$$\to m ^ {e * d_q} - m = k * q$$

$$\to q = gcd(n, k *q) = gcd(n, m ^ {e * d_q})$$

$$q = gcd(q * p, k * q)$$

Từ đó ta có thể tìm ra cả q. Từ q, co p = n // q, phi = (n // q - 1) * (q - 1)

(Không biết viết gì nữa nhưng vẫn cố viết cái gì đó vào đây để cho nó nhìn dài dài ra một tý mặc dù nó chẳng có tác dụng gì.Bị anh Tuệ dí gắt quá nên cố viết vào cho dài :>)
   
## PART_3. Write up

### RSA_1
---

**_Introduction:_**

Trong RSA, phép tính lũy thừa module là phép tính thường được sử dụng để tạo ra hàm bẫy (cùng với bài toán phân tích thừa số nguyên tố). Nó rất dễ thực hiện theo chiều xuôi nhưng gần như bất khả thi nếu tính theo chiều ngược (không có thông tin cần thiết).
Về mặt bản chất nó chỉ là phép lấy lũy thừa rồi lấy phần dư của nó khi chi cho n.

**_Task:_**

Find: pow(101, 27, 22663)

---

```python

print(pow(101, 17, 22663))

```

> 19906


### RSA_2

---

**_Introduction:_**

Mã hóa RSA gồm có n = q * p với p, q là hai số nguyên tố và e (thường là 2 ^ 16 + 1). Một bộ khóa công khai gồm có (n, e)
Với m là bản rõ ta mã hóa như sau : c = pow(m, e, n)

**_Task:_**

Mã hóa m = 12, p = 17, q = 23, e = 65537

---

Theo công thức trên ta dễ có c = pow(m, e, q * p)

> 301


### RSA_3

---

**_Introduction:_**

Trong RSA ta cần phải tính Phi(n) khi biết n. Đây là một bài toán khó khi n đủ lớn.

Giả sử: n = a^n * b^m * c^e ... (a, b, c là số nguyên tố)

=> phi(n) = n(1 - 1/a)(1 - 1/b)(1 - 1/c)

cũng tương tụ như thế với các n khác.

**_Task:_**

+ p = 857504083339712752489993810777
+ q = 1029224947942998075080348647219

tìm phi(n)

---

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

print((p - 1)*(q - 1))

> 882564595536224140639625987657529300394956519977044270821168


### RSA_4

---

+ $p = 857504083339712752489993810777$
+ $q = 1029224947942998075080348647219$
+ $e = 65537$

$\to \quad d = ?$

---

ta tìm $d$ bằng cách lấy $d \equiv e ^ {-1} \pmod{phi}$ với $phi = (p - 1) * (q - 11)$

```python

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi = (p - 1)*(q - 1)
print("d: ", pow(e, -1, phi))

```

=> 121832886702415731577073962957377780195510499965398469843281


### RSA_5

---

**_Description:_**

+ N = 882564595536224140639625987659416029426239230804614613279163
+ e = 65537
+ c = 77578995801157823671636298847186723593814843845525223303932
  
decrypt this

---

Ta có thể dễ dàng mã hóa như sau $c = m ^ e \pmod{n}$ và giải mã bằng $m = c ^ d \pmod{n}$ 

```python

from factordb.factordb import FactorDB
from Crypto.Util.number import *

N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932

f = FactorDB(N)
f.connect()
lst = f.get_factor_list()
phi = (lst[1] - 1) * (lst[0] - 1)
d = pow(e, -1, phi)

print(pow(c, d, N))


```


### RSA6

---

**_Descriptions:_**

Trên thực tế các tin nhắn mỗi khi được mã hóa sẽ được gửi đi kèm với cả bản rõ được hash để xác nhận. Các bước như sau:
  + B1: mã hóa tin nhắn c = m^e (mod n)
  + B2: sử dụng hàm băm cho m (với hàm băm thì thường dc chọn là md5, sha 256 vì nó có tính vảo mật cao và dễ tiếp cận)
  + B3 s = ( H(m) )^d (mod n)
  + B4: Gửi cả cặp (c, s)

Dễ thấy do s = (H(m))^d (mod n) nên ta có thể tính H(m) = s^e mod n. Sử sụng kết quả m = c^d (mod n) nếu H(m) == h(m) thì đây là tin nhắn đúng.

**_Task_**

Sign the flag crypto{Immut4ble_m3ssag1ng} using your private key and the SHA256 hash function.

Challenge files:
  - [private.key](https://cryptohack.org/static/challenges/private_0a1880d1fffce9403686130a1f932b10.key)

---


```python


from factordb.factordb import FactorDB
from Crypto.Util.number import *
from hashlib import sha256


def main():
    flag = "crypto{Immut4ble_m3ssag1ng}"
    hash = bytes_to_long(flag.encode())

    hash_func = sha256()
    hash_func.update(flag.encode())

    txt = open("private", "r").read().split("\n")
    N = txt[0][4:]
    d = txt[1][4:]
    enc = pow(int(hash_func.hexdigest(), 16), int(d), int(N))

    print("enc:", enc)

if __name__ == "__main__":
    main()



```


### RSA_7

---

**_TASK_**

Factorise the 150-bit number 510143758735509025530880200653196460532653147 into its two constituent primes. Give the smaller one as your answer.

---

Mình phân tích số nguyên tố trên factorDB thì dễ dàng ra được đáp án.

```python


from factordb.factordb import FactorDB

def main():
    N = 510143758735509025530880200653196460532653147

    primes = FactorDB(N)
    primes.connect()
    print(min(primes.get_factor_list()))
    

if __name__ == "__main__":
    main()



```



### RSA_8

---

**_TASK_**

Here is my super-strong RSA implementation, because it's 1600 bits strong it should be unbreakable... at least I think so!

Challenge files:
  - [inferius.py](https://cryptohack.org/static/challenges/inferius_e85eea9b19cd68aa71ce850918302bad.py)
  - [output.txt](https://cryptohack.org/static/challenges/output_4b843d94b6196df152219c3165b9347f.txt)

---

Bài này mình cũng phân tích bằng factorDB và dễ dàng có dc đáp án.

```python


from factordb.factordb import *
from Crypto.Util.number import *

def main():
    txt = open("output.txt", "r").read().split("\n")

    n = int(txt[0][4:])
    e = 3
    ct = int(txt[2][5:])

    primes = FactorDB(n)
    primes.connect()
    lst = primes.get_factor_list()

    phi = (lst[0] - 1) * (lst[1] - 1)

    print(long_to_bytes(pow(ct, pow(e, -1, phi), n)).decode())



if __name__ == "__main__":
    main()


```


### RSA_9

---
**_TASK_**

Why is everyone so obsessed with multiplying two primes for RSA. Why not just use one?

Challenge files:
  - [output.txt](https://cryptohack.org/static/challenges/output_086036e35349a406b94bfac9a7af6cca.txt)

---

Do bài này n là một số nguyên tố nên ta có thể tính phi = n - 1, sau đó tìm d rồi dễ dàng có flag.

```python


from Crypto.Util.number import *

def main():
    txt = open("output.txt", "r").read().split(" ")

    e = 65537
    n = int(txt[2])
    ct = int(txt[-3])

    print(long_to_bytes(pow(ct, pow(e, -1, n -1), n)).decode())

if __name__ == "__main__":
    main()


```


### RSA_10

---

**_TASK_**

It was taking forever to get a 2048 bit prime, so I just generated one and used it twice.

 If you're stuck, look again at the formula for Euler's totient.
Challenge files:
  - [output.txt](https://cryptohack.org/static/challenges/output_00dace150c0bc52f7abf03fc3e9529d2.txt)

---

Có n là bình phương của một số nên ta áp dụng công thức tính phi = n * (n - 1), từ đó giải quyết xong bài này.

```python


from gmpy2 import iroot
from Crypto.Util.number import *

def main():
    txt = open("output.txt", "r").read().split("\n")

    n = int(txt[0][4:])
    e = 65537
    ct = int(txt[2][5:])
    
    prime = iroot(n, 2)[0]

    assert prime ** 2 == n

    phi = prime * (prime - 1)

    print(long_to_bytes(pow(ct, pow(e, -1, phi), n)).decode())

if __name__ == "__main__":
    main()


```


### RSA_11

---

**_TASK_**

Using one prime factor was definitely a bad idea so I'll try using over 30 instead.

 If it's taking forever to factorise, read up on factorisation algorithms and make sure you're using one that's optimised for this scenario.


Challenge files:
  - [output.txt](https://cryptohack.org/static/challenges/output_5a478a5d4764257d0bbdfaed340fcbdd.txt)
    
---

Mình thử phân tích trên factorDB thì dễ dàng có được factor của n. Từ đó tính phi rồi dễ dàng có flag.

```python


from gmpy2 import iroot
from Crypto.Util.number import *
from factordb.factordb import *

def main():
    txt = open("output.txt", "r").read().split("\n")

    n = int(txt[0][4:])
    e = 65537
    ct = int(txt[2][5:])
    
    primes = FactorDB(n)
    primes.connect()
    primes = primes.get_factor_list()

    phi = 1
    for x in primes:
        phi *= x - 1

    print(long_to_bytes(pow(ct, pow(e, -1, phi), n)).decode())

if __name__ == "__main__":
    main()


```


### RSA_12

---

**_TASK_**

Smallest exponent should be fastest, right?

Challenge files:
  - [salty.py](https://cryptohack.org/static/challenges/salty_9854bdcadc3f8b8f58008a24d392c1bf.py)
  - [output.txt](https://cryptohack.org/static/challenges/output_95f558e889cc66920c24a961f1fb8181.txt)

---

Bài này cx khá hay, có e = 1 nên phép mũ trở nên vô dụng mà n lại quá lớn khi so với plaintext nên ta có flag không thay đổi.

```python


from gmpy2 import iroot
from Crypto.Util.number import *
from factordb.factordb import *

def main():
    txt = open("output.txt", "r").read().split(" ")

    e = 1
    n = txt[2]
    ct = txt[-1][:-1]

    print(long_to_bytes(int(ct)).decode())
    

if __name__ == "__main__":
    main()


```


### RSA_13

---

**_TASK_**

My primes should be more than large enough now!

Challenge files:
  - modulus_inutilis.py
  - output.txt

---

Bài này cũng khá giống bài trên nhưng do e là mã 3 nên ta lấy căn bậc 3 là xong(n quá lớn so với plaintext nên phép mod k có tác dụngdụng)

```python


from gmpy2 import iroot
from Crypto.Util.number import *

def main():
    txt = open("output.txt", "r").read().split("\n")
    ct = int(txt[2][5:])
    print(long_to_bytes(iroot(ct, 3)[0]).decode())

    

if __name__ == "__main__":
    main()


```


### RSA_14

---

**_TASK_**

We have a supercomputer at work, so I've made sure my encryption is secure by picking massive numbers!

Challenge files:
  - source.py
  - output.txt

---

Khi xem file source mình thấy, thay vì tìm d từ e như bình thường thì ở đây ta tìm e từ d. Dễ thấy, e.bit_length == n.bit_length nên d nhỏ , từ đó nghĩ tới tấn công low private exponent.

```sage

from __future__ import print_function
import time

############################################
# Config
##########################################

"""
Setting debug to true will display more informations
about the lattice, the bounds, the vectors...
"""
debug = True

"""
Setting strict to true will stop the algorithm (and
return (-1, -1)) if we don't have a correct
upperbound on the determinant. Note that this
doesn't necesseraly mean that no solutions
will be found since the theoretical upperbound is
usualy far away from actual results. That is why
you should probably use `strict = False`
"""
strict = False

"""
This is experimental, but has provided remarkable results
so far. It tries to reduce the lattice as much as it can
while keeping its efficiency. I see no reason not to use
this option, but if things don't work, you should try
disabling it
"""
helpful_only = True
dimension_min = 7 # stop removing if lattice reaches that dimension

############################################
# Functions
##########################################

# display stats on helpful vectors
def helpful_vectors(BB, modulus):
    nothelpful = 0
    for ii in range(BB.dimensions()[0]):
        if BB[ii,ii] >= modulus:
            nothelpful += 1

    print(nothelpful, "/", BB.dimensions()[0], " vectors are not helpful")

# display matrix picture with 0 and X
def matrix_overview(BB, bound):
    for ii in range(BB.dimensions()[0]):
        a = ('%02d ' % ii)
        for jj in range(BB.dimensions()[1]):
            a += '0' if BB[ii,jj] == 0 else 'X'
            if BB.dimensions()[0] < 60:
                a += ' '
        if BB[ii, ii] >= bound:
            a += '~'
        print(a)

# tries to remove unhelpful vectors
# we start at current = n-1 (last vector)
def remove_unhelpful(BB, monomials, bound, current):
    # end of our recursive function
    if current == -1 or BB.dimensions()[0] <= dimension_min:
        return BB

    # we start by checking from the end
    for ii in range(current, -1, -1):
        # if it is unhelpful:
        if BB[ii, ii] >= bound:
            affected_vectors = 0
            affected_vector_index = 0
            # let's check if it affects other vectors
            for jj in range(ii + 1, BB.dimensions()[0]):
                # if another vector is affected:
                # we increase the count
                if BB[jj, ii] != 0:
                    affected_vectors += 1
                    affected_vector_index = jj

            # level:0
            # if no other vectors end up affected
            # we remove it
            if affected_vectors == 0:
                print("* removing unhelpful vector", ii)
                BB = BB.delete_columns([ii])
                BB = BB.delete_rows([ii])
                monomials.pop(ii)
                BB = remove_unhelpful(BB, monomials, bound, ii-1)
                return BB

            # level:1
            # if just one was affected we check
            # if it is affecting someone else
            elif affected_vectors == 1:
                affected_deeper = True
                for kk in range(affected_vector_index + 1, BB.dimensions()[0]):
                    # if it is affecting even one vector
                    # we give up on this one
                    if BB[kk, affected_vector_index] != 0:
                        affected_deeper = False
                # remove both it if no other vector was affected and
                # this helpful vector is not helpful enough
                # compared to our unhelpful one
                if affected_deeper and abs(bound - BB[affected_vector_index, affected_vector_index]) < abs(bound - BB[ii, ii]):
                    print("* removing unhelpful vectors", ii, "and", affected_vector_index)
                    BB = BB.delete_columns([affected_vector_index, ii])
                    BB = BB.delete_rows([affected_vector_index, ii])
                    monomials.pop(affected_vector_index)
                    monomials.pop(ii)
                    BB = remove_unhelpful(BB, monomials, bound, ii-1)
                    return BB
    # nothing happened
    return BB

""" 
Returns:
* 0,0   if it fails
* -1,-1 if `strict=true`, and determinant doesn't bound
* x0,y0 the solutions of `pol`
"""
def boneh_durfee(pol, modulus, mm, tt, XX, YY):
    """
    Boneh and Durfee revisited by Herrmann and May
    
    finds a solution if:
    * d < N^delta
    * |x| < e^delta
    * |y| < e^0.5
    whenever delta < 1 - sqrt(2)/2 ~ 0.292
    """

    # substitution (Herrman and May)
    PR.<u, x, y> = PolynomialRing(ZZ)
    Q = PR.quotient(x*y + 1 - u) # u = xy + 1
    polZ = Q(pol).lift()

    UU = XX*YY + 1

    # x-shifts
    gg = []
    for kk in range(mm + 1):
        for ii in range(mm - kk + 1):
            xshift = x^ii * modulus^(mm - kk) * polZ(u, x, y)^kk
            gg.append(xshift)
    gg.sort()

    # x-shifts list of monomials
    monomials = []
    for polynomial in gg:
        for monomial in polynomial.monomials():
            if monomial not in monomials:
                monomials.append(monomial)
    monomials.sort()
    
    # y-shifts (selected by Herrman and May)
    for jj in range(1, tt + 1):
        for kk in range(floor(mm/tt) * jj, mm + 1):
            yshift = y^jj * polZ(u, x, y)^kk * modulus^(mm - kk)
            yshift = Q(yshift).lift()
            gg.append(yshift) # substitution
    
    # y-shifts list of monomials
    for jj in range(1, tt + 1):
        for kk in range(floor(mm/tt) * jj, mm + 1):
            monomials.append(u^kk * y^jj)

    # construct lattice B
    nn = len(monomials)
    BB = Matrix(ZZ, nn)
    for ii in range(nn):
        BB[ii, 0] = gg[ii](0, 0, 0)
        for jj in range(1, ii + 1):
            if monomials[jj] in gg[ii].monomials():
                BB[ii, jj] = gg[ii].monomial_coefficient(monomials[jj]) * monomials[jj](UU,XX,YY)

    # Prototype to reduce the lattice
    if helpful_only:
        # automatically remove
        BB = remove_unhelpful(BB, monomials, modulus^mm, nn-1)
        # reset dimension
        nn = BB.dimensions()[0]
        if nn == 0:
            print("failure")
            return 0,0

    # check if vectors are helpful
    if debug:
        helpful_vectors(BB, modulus^mm)
    
    # check if determinant is correctly bounded
    det = BB.det()
    bound = modulus^(mm*nn)
    if det >= bound:
        print("We do not have det < bound. Solutions might not be found.")
        print("Try with highers m and t.")
        if debug:
            diff = (log(det) - log(bound)) / log(2)
            print("size det(L) - size e^(m*n) = ", floor(diff))
        if strict:
            return -1, -1
    else:
        print("det(L) < e^(m*n) (good! If a solution exists < N^delta, it will be found)")

    # display the lattice basis
    if debug:
        matrix_overview(BB, modulus^mm)

    # LLL
    if debug:
        print("optimizing basis of the lattice via LLL, this can take a long time")

    BB = BB.LLL()

    if debug:
        print("LLL is done!")

    # transform vector i & j -> polynomials 1 & 2
    if debug:
        print("looking for independent vectors in the lattice")
    found_polynomials = False
    
    for pol1_idx in range(nn - 1):
        for pol2_idx in range(pol1_idx + 1, nn):
            # for i and j, create the two polynomials
            PR.<w,z> = PolynomialRing(ZZ)
            pol1 = pol2 = 0
            for jj in range(nn):
                pol1 += monomials[jj](w*z+1,w,z) * BB[pol1_idx, jj] / monomials[jj](UU,XX,YY)
                pol2 += monomials[jj](w*z+1,w,z) * BB[pol2_idx, jj] / monomials[jj](UU,XX,YY)

            # resultant
            PR.<q> = PolynomialRing(ZZ)
            rr = pol1.resultant(pol2)

            # are these good polynomials?
            if rr.is_zero() or rr.monomials() == [1]:
                continue
            else:
                print("found them, using vectors", pol1_idx, "and", pol2_idx)
                found_polynomials = True
                break
        if found_polynomials:
            break

    if not found_polynomials:
        print("no independant vectors could be found. This should very rarely happen...")
        return 0, 0
    
    rr = rr(q, q)

    # solutions
    soly = rr.roots()

    if len(soly) == 0:
        print("Your prediction (delta) is too small")
        return 0, 0

    soly = soly[0][0]
    ss = pol1(q, soly)
    solx = ss.roots()[0][0]

    #
    return solx, soly

def example():
    ############################################
    # How To Use This Script
    ##########################################

    #
    # The problem to solve (edit the following values)
    #
    N = 0xb8af3d3afb893a602de4afe2a29d7615075d1e570f8bad8ebbe9b5b9076594cf06b6e7b30905b6420e950043380ea746f0a14dae34469aa723e946e484a58bcd92d1039105871ffd63ffe64534b7d7f8d84b4a569723f7a833e6daf5e182d658655f739a4e37bd9f4a44aff6ca0255cda5313c3048f56eed5b21dc8d88bf5a8f8379eac83d8523e484fa6ae8dbcb239e65d3777829a6903d779cd2498b255fcf275e5f49471f35992435ee7cade98c8e82a8beb5ce1749349caa16759afc4e799edb12d299374d748a9e3c82e1cc983cdf9daec0a2739dadcc0982c1e7e492139cbff18c5d44529407edfd8e75743d2f51ce2b58573fea6fbd4fe25154b9964d
    e = 0x9ab58dbc8049b574c361573955f08ea69f97ecf37400f9626d8f5ac55ca087165ce5e1f459ef6fa5f158cc8e75cb400a7473e89dd38922ead221b33bc33d6d716fb0e4e127b0fc18a197daf856a7062b49fba7a86e3a138956af04f481b7a7d481994aeebc2672e500f3f6d8c581268c2cfad4845158f79c2ef28f242f4fa8f6e573b8723a752d96169c9d885ada59cdeb6dbe932de86a019a7e8fc8aeb07748cfb272bd36d94fe83351252187c2e0bc58bb7a0a0af154b63397e6c68af4314601e29b07caed301b6831cf34caa579eb42a8c8bf69898d04b495174b5d7de0f20cf2b8fc55ed35c6ad157d3e7009f16d6b61786ee40583850e67af13e9d25be3

    # the hypothesis on the private exponent (the theoretical maximum is 0.292)
    delta = .18 # this means that d < N^delta

    #
    # Lattice (tweak those values)
    #

    # you should tweak this (after a first run), (e.g. increment it until a solution is found)
    m = 4 # size of the lattice (bigger the better/slower)

    # you need to be a lattice master to tweak these
    t = int((1-2*delta) * m)  # optimization from Herrmann and May
    X = 2*floor(N^delta)  # this _might_ be too much
    Y = floor(N^(1/2))    # correct if p, q are ~ same size

    #
    # Don't touch anything below
    #

    # Problem put in equation
    P.<x,y> = PolynomialRing(ZZ)
    A = int((N+1)/2)
    pol = 1 + x * (A + y)

    #
    # Find the solutions!
    #

    # Checking bounds
    if debug:
        print("=== checking values ===")
        print("* delta:", delta)
        print("* delta < 0.292", delta < 0.292)
        print("* size of e:", int(log(e)/log(2)))
        print("* size of N:", int(log(N)/log(2)))
        print("* m:", m, ", t:", t)

    # boneh_durfee
    if debug:
        print("=== running algorithm ===")
        start_time = time.time()

    solx, soly = boneh_durfee(pol, e, m, t, X, Y)

    # found a solution?
    if solx > 0:
        print("=== solution found ===")
        if False:
            print("x:", solx)
            print("y:", soly)

        d = int(pol(solx, soly) / e)
        print("private key found:", d)
    else:
        print("=== no solution was found ===")

    if debug:
        print(("=== %s seconds ===" % (time.time() - start_time)))

if __name__ == "__main__":
    example()

```

```python


from Crypto.Util.number import *

def main():
    txt = open("output.txt", "r").read().split("\n")

    n = int(txt[0][4:], 16)
    e = txt[1][4:]
    c = int(txt[2][4:], 16)

    d = 79434351637397000170240219617391501050474168352481334243649813782018808904459

    print(long_to_bytes(pow(c, d, n)))
    


if __name__ == "__main__":
    main()



```


### RSA_15

---

**_TASK_**

Crossed Wires 100 pts · 2470 Solves

I asked my friends to encrypt our secret flag before sending it to me, but instead of using my key, they've all used their own! Can you help?

Challenge files:
  - source.py
  - output.txt

---

Bài này sử dụng mã hóa nhiều là và dùng chung một n khác các e. Ta tìm phi từ d và e đã có rồi lần lượt mã hóa ngược lại flag.Cụ thể như sau:

$$e * d = 1 \pmod{phi} \to \quad e * d = k * phi + 1\to phi = (e * d - 1)/k \forall k \in R $$

Brute tìm ra phi rồi từ phi với các e đã biết ta có thể tìm ra d rồi mã hóa ra flag như đã viết.

```python


from Crypto.Util.number import *

def main():
    private_key =  (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 2734411677251148030723138005716109733838866545375527602018255159319631026653190783670493107936401603981429171880504360560494771017246468702902647370954220312452541342858747590576273775107870450853533717116684326976263006435733382045807971890762018747729574021057430331778033982359184838159747331236538501849965329264774927607570410347019418407451937875684373454982306923178403161216817237890962651214718831954215200637651103907209347900857824722653217179548148145687181377220544864521808230122730967452981435355334932104265488075777638608041325256776275200067541533022527964743478554948792578057708522350812154888097)
    public_keys = [(21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 106979), (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 108533), (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 69557), (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 97117), (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 103231)]
    c = 20304610279578186738172766224224793119885071262464464448863461184092225736054747976985179673905441502689126216282897704508745403799054734121583968853999791604281615154100736259131453424385364324630229671185343778172807262640709301838274824603101692485662726226902121105591137437331463201881264245562214012160875177167442010952439360623396658974413900469093836794752270399520074596329058725874834082188697377597949405779039139194196065364426213208345461407030771089787529200057105746584493554722790592530472869581310117300343461207750821737840042745530876391793484035024644475535353227851321505537398888106855012746117
    
    N = private_key[0]
    d = private_key[1]


    e = 0x10001
    # ed = 1 + kphi

    t = True
    k = 1
    while t:
        phi = round((e * d - 1) // k)

        if d == pow(e, -1, phi):
            t = False
        else:
            k += 1

    for x in range(4, -1, -1):
        c = pow(c, pow(public_keys[x][1], -1, phi), N)

    print(long_to_bytes(c))


if __name__ == "__main__":
    main()



```


## RSA_16

---

**_TASK_**

Okay so I got a bit carefree with my last script, but this time I've protected myself while keeping everything really big. Nothing will stop me and my supercomputer now!

Challenge files:
  - source.py
  - output.txt

---

Bài này mình sử dụng FActorDB nên dễ ràng có flag.

```python


import owiener
from factordb.factordb import FactorDB
from gmpy2 import iroot
from Crypto.Util.number import *

def main():

    dict = {}
    txt = open("output.txt", "r").read().split("\n")

    
    for line in txt:
        tmp = line.split(" = ")
        dict[tmp[0]] = int(tmp[1], 16)

    primes = FactorDB(dict["N"])
    primes.connect()
    lst = primes.get_factor_list()

    phi = (lst[0] - 1) * (lst[1] - 1)

    print(long_to_bytes(pow(dict["c"], pow(dict["e"], -1, phi), dict["N"])).decode())


if __name__ == "__main__":
    main()



```


```python



```



### RSA_17

----

**_TASK:_**

Poor Johan has been answering emails all day and the students are all asking the same questions. Can you read his messages?

Challenge files:
  - johan.py
  - output.txt

----

Bài này sử dụng CRT vì tất cả các mũ e đểu bằng nhau. Từ đó ta có được $m^3$ việc còn lại chỉ là tìm căn nó mà thôi :>

```python


from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

txt = open("output.txt", "r").read().split("\n\n")

e = 3
lst = {}
t = 0

for i in txt:
    tmp = {}
    for x in i.split("\n"):
        if x != "":
            tmp[x.split(" = ")[0]] = int(x.split(" = ")[1])
    lst[t] = tmp
    t += 1

# n is modulus, a is remainder
def CRT(n: list, a: list) -> int:
    p = 1
    for i in n:
        p *= i
    sm = 0
    for i in range(len(n)):
        pp = p // n[i]
        sm += (a[i] * pow(pp, -1, n[i]) * pp) % p
    return sm % p

for x in range(7):
    for y in range(x + 1, 7):
        for z in range(y + 1, 7):
            n = [lst[x]["n"], lst[y]["n"], lst[z]["n"]]
            a = [lst[x]["c"], lst[y]["c"], lst[z]["c"]]

            c = CRT(n, a)

            m = long_to_bytes(iroot(c, e)[0])
            if b"crypto{" in m:
                print(m.decode())
                exit()

```


### RSA_18

---

**_TASK:_**

Finding large primes is slow, so I've devised an optimisation.

Challenge files:
  - descent.py
  - output.txt

---

Do bài này ta dễ thấy hai số q, p là hai số nguyên tố gần nên nghĩ ngay tới việc sử dụng Fermat attack(nếu bạn cảm thấy nó khó hiểu như anh Tuệ thì có thể đọc giải thích mình đã viết ở trên). Sau đó mình có được q, p nên dễ dàng tìm ra được flag.

```python


from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot

def main():
    
    txt = open('output.txt', 'r').read().split('\n')
    dict = {}
    for i in txt:
        if i != '':
            dict[i.split(' = ')[0]] = int(i.split(' = ')[1])
    
    def Fermat_attack(n):
        a = iroot(n, 2)[0] + 1
        b = iroot(a * a - n, 2)[0]
        while n != a**2 - b**2:
            a += 1
            b = a * a - n

        return (a+b, a-b)
    
    p, q = Fermat_attack(dict['n'])
    print(f"p = {p}")
    print(f"q = {q}")

    phi = (p-1) * (q-1)
    d = pow(dict['e'], -1, phi)
    print(long_to_bytes(pow(dict['c'], d, dict['n'])).decode())


if __name__ == '__main__':
    main()



```

### RSA_19

---
**_Description:_**
I've found a super fast way to generate primes from my secret list.

Challenge files:
  - [marin.py](https://cryptohack.org/static/challenges/marin_15d882fcfd597e1fb7785379b2529875.py)
  - [output.txt](https://cryptohack.org/static/challenges/output_f194012343666ced1a6699d196c8adc5.txt)

---

Bài này nói đến cách tạo số nt từ 2^n - 1. Đây là một cách khá là dễ để phá vì hiện nay có khoảng 50 số nt đã biết từ nó.

C1: Lên Factordb thì dc luôn q, p

C2:
Khi dùng

```python
      print(len(bin(n)[2:]))
```

thì dc len_bit của n là 4484. Mà:
  + các số q và q không dc quá gần nhau hoặc bằng nhau vì sẽ ảnh hưởng đến tính bảo mật
  + các số q và p không dc quá xa nhau vì nó cx có thể dễ ràng brute

từ đó q ~ P => len_bit(q) ~ len_bit(p)

từ đó len__bit(q) nằm trong khoảng 2048 -> 2242. Do có ít khả năng nên hướng tới quá trình brute tất cả q

```python


from Crypto.Util.number import *
from tqdm import tqdm
# from secret import secrets, flag

n = 658416274830184544125027519921443515789888264156074733099244040126213682497714032798116399288176502462829255784525977722903018714434309698108208388664768262754316426220651576623731617882923164117579624827261244506084274371250277849351631679441171018418018498039996472549893150577189302871520311715179730714312181456245097848491669795997289830612988058523968384808822828370900198489249243399165125219244753790779764466236965135793576516193213175061401667388622228362042717054014679032953441034021506856017081062617572351195418505899388715709795992029559042119783423597324707100694064675909238717573058764118893225111602703838080618565401139902143069901117174204252871948846864436771808616432457102844534843857198735242005309073939051433790946726672234643259349535186268571629077937597838801337973092285608744209951533199868228040004432132597073390363357892379997655878857696334892216345070227646749851381208554044940444182864026513709449823489593439017366358869648168238735087593808344484365136284219725233811605331815007424582890821887260682886632543613109252862114326372077785369292570900594814481097443781269562647303671428895764224084402259605109600363098950091998891375812839523613295667253813978434879172781217285652895469194181218343078754501694746598738215243769747956572555989594598180639098344891175879455994652382137038240166358066403475457 
e = 65537
c =  400280463088930432319280359115194977582517363610532464295210669530407870753439127455401384569705425621445943992963380983084917385428631223046908837804126399345875252917090184158440305503817193246288672986488987883177380307377025079266030262650932575205141853413302558460364242355531272967481409414783634558791175827816540767545944534238189079030192843288596934979693517964655661507346729751987928147021620165009965051933278913952899114253301044747587310830419190623282578931589587504555005361571572561916866063458812965314474160499067525067495140150092119620928363007467390920130717521169105167963364154636472055084012592138570354390246779276003156184676298710746583104700516466091034510765027167956117869051938116457370384737440965109619578227422049806566060571831017610877072484262724789571076529586427405780121096546942812322324807145137017942266863534989082115189065560011841150908380937354301243153206428896320576609904361937035263985348984794208198892615898907005955403529470847124269512316191753950203794578656029324506688293446571598506042198219080325747328636232040936761788558421528960279832802127562115852304946867628316502959562274485483867481731149338209009753229463924855930103271197831370982488703456463385914801246828662212622006947380115549529820197355738525329885232170215757585685484402344437894981555179129287164971002033759724456


def get_prime(secret):
    prime = 1
    for _ in range(secret):
        prime = prime << 1
    return prime - 1

len_bit = 2048

for l in tqdm(range(2048, 4484), desc="Bit length"):
    p = get_prime(l)
    if isPrime(n//p):
        q = n//p
        break

print()
print("P:", p)
print("Q:", q)

phi = (q - 1) * (p - 1)

d =pow(e, -1, phi)

print(long_to_bytes(pow(c, d, n)))

```


> crypto{Th3se_Pr1m3s_4r3_t00_r4r3}


### RSA_20

---

**_TASK:_**

I need to produce millions of RSA keys quickly and the standard way just doesn't cut it. Here's yet another fast way to generate primes which has actually resisted years of review.

Challenge files:
  - fast_primes.py
  - key.pem
  - ciphertext.txt

---


![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/9077923a-4341-46c7-ad16-0451c96d1f38)


```python


from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB
from Crypto.Cipher import PKCS1_OAEP

c = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28

txt = open('key.pem', 'r').read()

n = vars(RSA.importKey(txt))
e = int(n['_e'])
n = int(n['_n'])
print(n)
print(c)
f = FactorDB(n)
f.connect()
p, q = f.get_factor_list()
print(p, q)

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
key = RSA.construct((n, e, d))

cipher = PKCS1_OAEP.new(key)
print(cipher.decrypt(long_to_bytes(c)))



```


### RSA_21

---
**_TASK:_**

Here's a bunch of RSA public keys I gathered from people on the net together with messages that they sent.

As excerpt.py shows, everyone was using PKCS#1 OAEP to encrypt their own messages. It shouldn't be possible to decrypt them, but perhaps there are issues with some of the keys?

Challenge files:
  - excerpt.py
  - keys_and_messages.zip

---

Khi đọc file đề mình thấy n, e được lưu ở file số 21 nên mở nó ra và việc còn lại để FactorDB lo.

```python



from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB
from Crypto.Cipher import PKCS1_OAEP

c = open('21.ciphertext', 'r').read()
c = int(c, 16)
txt = open('21.pem', 'r').read()
n = vars(RSA.importKey(txt))
e = int(n['_e'])
n = int(n['_n'])

f = FactorDB(n)
f.connect()
p, q = f.get_factor_list()


phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
key = RSA.construct((n, e, d))

cipher = PKCS1_OAEP.new(key)
print(cipher.decrypt(long_to_bytes(c)))




```

### RSA_22

---

**_TASK:_**

RSA Backdoor Viability175 pts · 940 Solves · 7 Solutions
It seems like my method to generate fast primes was not completely secure. I came up with a new approach to improve security, including a factorization backdoor in case I ever lose my private key. You'll definitely need some complex techniques to break this!

You may need to tweak the recursion limit (sys.setrecursionlimit(n) in Python) in your programming language to get your solution working.

Challenge files:
  - complex_primes.py
  - output.txt

---

Haizz, bài này nên làm theo cách tấn công 4p - 1, nhưng do nó khá khó nên factordb luôn cho nhanh. $\to$ solution:

```py
n = 709872443186761582125747585668724501268558458558798673014673483766300964836479167241315660053878650421761726639872089885502004902487471946410918420927682586362111137364814638033425428214041019139158018673749256694555341525164012369589067354955298579131735466795918522816127398340465761406719060284098094643289390016311668316687808837563589124091867773655044913003668590954899705366787080923717270827184222673706856184434629431186284270269532605221507485774898673802583974291853116198037970076073697225047098901414637433392658500670740996008799860530032515716031449787089371403485205810795880416920642186451022374989891611943906891139047764042051071647203057520104267427832746020858026150611650447823314079076243582616371718150121483335889885277291312834083234087660399534665835291621232056473843224515909023120834377664505788329527517932160909013410933312572810208043849529655209420055180680775718614088521014772491776654380478948591063486615023605584483338460667397264724871221133652955371027085804223956104532604113969119716485142424996255737376464834315527822566017923598626634438066724763559943441023574575168924010274261376863202598353430010875182947485101076308406061724505065886990350185188453776162319552566614214624361251463
e = 65537
c = 608484617316138126443275660524263025508135383745665175433229598517433030003704261658172582370543758277685547533834085899541036156595489206369279739210904154716464595657421948607569920498815631503197235702333017824993576326860166652845334617579798536442066184953550975487031721085105757667800838172225947001224495126390587950346822978519677673568121595427827980195332464747031577431925937314209391433407684845797171187006586455012364702160988147108989822392986966689057906884691499234298351003666019957528738094330389775054485731448274595330322976886875528525229337512909952391041280006426003300720547721072725168500104651961970292771382390647751450445892361311332074663895375544959193148114635476827855327421812307562742481487812965210406231507524830889375419045542057858679609265389869332331811218601440373121797461318931976890674336807528107115423915152709265237590358348348716543683900084640921475797266390455366908727400038393697480363793285799860812451995497444221674390372255599514578194487523882038234487872223540513004734039135243849551315065297737535112525440094171393039622992561519170849962891645196111307537341194621689797282496281302297026025131743423205544193536699103338587843100187637572006174858230467771942700918388

from factordb.factordb import FactorDB
from Crypto.Util.number import *

f = FactorDB(n)
f.connect()
factors = f.get_factor_list()
phi = (factors[0]-1)*(factors[1]-1)

d = pow(e,-1,phi)
m = pow(c,d,n)
print(long_to_bytes(m).decode())
```

### RSA_23

---

**_TASK:_**

Been cooking up my own padding scheme, now my encrypted flag is different everytime!

*Connect at socket.cryptohack.org 13386*

Challenge files:
  - 13386.py

---

Ở bài này, ta có cách pad là thêm với hệ số a, b. Có:
$$(a_1 * m + b_1) ^ {e} = c_1 \pmod{n} \quad \to \quad p_1 \equiv (a_1 * m + b_1) ^ {e} - c_1 \equiv 0 \pmod{n}$$
$$(a_2 * m + b_2) ^ {e} = c_2 \pmod{n} \quad \to \quad p_2 \equiv (a_2 * m + b_2) ^ {e} - c_2 \equiv 0 \pmod{n}$$

Vì cả hai hệ có chung một nghiệm là $m$ nên khi lấy $GCD(p_1, p_2)$ thì ta sẽ có được m. Để lấy được gcd của đa thức ta có thể sử dụng Euclidean algorithm.
$$a * p_1 + b * p_2 = gcd(p_1, p_2) \quad \forall a, b \in R$$

Ở đây do là đa thức nên $gcd(p_1, p_2)$ là đa thức dạng $k_1 * x + k_2$ nên từ đó $m = x = (- k_1) / k_2$ (do ở đây m > 0 nên m = - x)
Lưu ý: ở đây các phép toán thực hiện trên vành $Z_n$ nên $x = - k_1 * (k_2 ^ {-1}) \pmod{n}$

```sage
a_1 = 17162007231311912596881232614414284740571306728000523153153762846286545376074086012523654088446930792099462138735407742618628486664616006556851336426277314769301631598994971630457155637948283420221868485142883718922854558204865140809223277632852739351273350855924655979528734043199315512490555039570608761303645621185410385318749549324039842614901771897248350574623112681957384483554126304956327481093113433223442718297718702324795580798509598781274423356651272077472783603775587956523948669656072595440147076072736371676165555415142029258405092390871403879531839340217564187257509039855732240398145484544346605825506
b_1 = 12728910801852701298970809601109654524922491804041092010050434271122411766892987878597259627022767997866889151096975076389054696347995631307043411737023346783907065169772873772265172639142174460272364031325439484800217565494390027358691863318312697896769976927921249381343221246914349154799903238818149231579375197882763299216957397563511535279541429521152771173889423075641631239264839901607264751672843333735891164084082700604529117503741410949551866711349282534827298443613070692341147302722062943746024874343442679263468809732766897329841510516420385829746157443521698397226391525213289197970493179369331127059699

a_2 = 7488481819371669186210556731106084122601862973062938343532438652077141932062154868189163309965447336722662602132566350094595550649262304111402632924611911919636242609617270988265066473854643941862502258088420468554283963747918237295579695891127184572342325948431745468930563458404711584023593078020031521258331655349905997812925292545296252277231587404242237406265276849813090884450895530156461008371312542853805271829141000531570843025492421416129659107165635466203688812254236880831445431721851270031246629651167948118778931356363926202461466490245912711233102946022205864153127202221669473407951943610758170718562
b_2 = 1943770981482450073372224968709345970535303551580082475401088843685495743786566631785398705868361931061287668750465547577225848297341413690238898566011471181061250598347256524653388630468415993603033410038149592691810101926763487440228792014681213054222791454814004946620879736626796823499853048753392148956522449179830411900541047426303444742400273278966118487916444005433251346408519079171489153551215730046825406936819496114873154050327610716827758805256831085717999851855878885776527749682831003316494376794185874654378057052558863037576083182061344248005831163603448805703272282330713377151035574579156369487350

e = 11
c_1 = 3722276538708576810135582049777478248813340811432584756132467807064633144228058244261014027805462706379206421557294827128333377534887742462848024475241771510404261716339105324995260590909819718947663657228556962878878019169666879948273245689060970205860940982267042612867030847164965306043093208403603388880717553528316616667314814082751655523995779195751728288849716760427237925104954249896401606687006993615133513456077317795932106263974234404342316111931833517106548058290087117176907887836047913996357797063110535413852432939928290238334679366552736667950604051935941076143600517086375128438282098905022393599577
c_2 = 24031855943401774334767271017064337592781917047838509046509038306915351130601883194171581570374966372572278802999431862592222537224061000493187294948998032678501284058090089782688485192579426690753106229383401152644971416324031438039461297772337428082734481347872570843248010236422203682931999398860551134846190319006024643541735887435306985424284437374197169517324890453212252847676706478608223107834689620572477322020606870103876417365657920440059012016776754883595463091476995948422576367220068209521215758204094833029612726587460062816060758843102652423359224636760685584592759559843623704703674396313561689400979

n = 24129274210542368779384136015071771494880097975591074545545673044790048274189069595459582260597453834458319903764639472243823895416855121993241499799234118491832840420755618977980472504718049617831316608135748918826935271899731685555927104413536534375298620741901072221797604839844921461052118301676173630376495811234070526248256879213740325006261231473679475014731322352117658991110338372805266727231433733705638249922274980480062560321384218681304616595672366936750515333394418888537608681967082453279049944482384051108141905460148368996896989298035169802747204154144677474269357629045746866037221439287152349065673

p.<x> = PolynomialRing(Zmod(n))

p1 = (a_1 * x + b_1) ** e - c_1
p2 = (a_2 * x + b_2) ** e - c_2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a, b
print(gcd(p1, p2))


```

từ đó có hệ : 
```
15068000529051858974078233360898083852193818548072020340539084206583920319536386103716279519612268531398253302027872144330590930409824142872801556648551378866011115469506758470874253127360289321588674927089408367112780137432977332580699968774082872839181756463593991599269897128345681118315607735333750877468017759361005970417195675538921140431599420640959687475306213540454503733372342073925895942554673306262669750236369225709140649164832667125240774427232023619752197599028617557973643697674715466931431141205127136887322106947602748705840849645592120252840202045061066517237362273475062572275482119401944734753348*x + 7780560773438608891664556743027867458399219523568634027517431612400044366352854217652618783450042970363103754853449465567768036765889830250341501857597567402217729624339502308105398319915637254989825849785954203481735887243614012485303719941404622682958459963328962178414960489403194324328015561647601260871762399397363709738312979828996153827239443621336934971902983562174912371837748010589880024241507399091503913428491088233458700565967923681221645748846274764417222911467652734779124555323943779689160138229072720450992403342875984393985654942966227066291733186007175014988487820487424927296366006117445400610137
```

```python
n = 24129274210542368779384136015071771494880097975591074545545673044790048274189069595459582260597453834458319903764639472243823895416855121993241499799234118491832840420755618977980472504718049617831316608135748918826935271899731685555927104413536534375298620741901072221797604839844921461052118301676173630376495811234070526248256879213740325006261231473679475014731322352117658991110338372805266727231433733705638249922274980480062560321384218681304616595672366936750515333394418888537608681967082453279049944482384051108141905460148368996896989298035169802747204154144677474269357629045746866037221439287152349065673

a = 15068000529051858974078233360898083852193818548072020340539084206583920319536386103716279519612268531398253302027872144330590930409824142872801556648551378866011115469506758470874253127360289321588674927089408367112780137432977332580699968774082872839181756463593991599269897128345681118315607735333750877468017759361005970417195675538921140431599420640959687475306213540454503733372342073925895942554673306262669750236369225709140649164832667125240774427232023619752197599028617557973643697674715466931431141205127136887322106947602748705840849645592120252840202045061066517237362273475062572275482119401944734753348
b = 7780560773438608891664556743027867458399219523568634027517431612400044366352854217652618783450042970363103754853449465567768036765889830250341501857597567402217729624339502308105398319915637254989825849785954203481735887243614012485303719941404622682958459963328962178414960489403194324328015561647601260871762399397363709738312979828996153827239443621336934971902983562174912371837748010589880024241507399091503913428491088233458700565967923681221645748846274764417222911467652734779124555323943779689160138229072720450992403342875984393985654942966227066291733186007175014988487820487424927296366006117445400610137
from Crypto.Util.number import long_to_bytes

print(long_to_bytes(-(b * pow(a, -1, n)) % n))

```

> crypto{linear_padding_isnt_padding}

### RSA_24

---

**_TASK:_**

Can custom padding save one from some of the mistakes we already covered?

Challenge files:
  - pad_encrypt.py
  - output.txt

---

Bài này mình sử dụng copper smith attack. Đã biết được một phần của flag là "crypto{" và "}" từ đó ta hướng tới việc tìm phần còn thiếu của flag.

flag = "crypto{" + "????????????????????????????" + "}" + "\x00\x00..."

đặt x = bytes_to_long(flag), 
c = bytes_to_long("crypto{" + "\x00\x00..." + "}" + "\x00\x00...")

từ đó đặt f(x) = ((m + (2 **(8 * 58)) * x) ** 3 - c)//(2 ** (8 * 58 * e))

với x là cái cần tìm tức đoạn flag còn chưa biết, ta chia cho (2 ** (8 * 58 * e)) là để giảm độ lớn của phép tính mà vẫn k ảnh hưởng tới tính chính xác. Việc còn lại là code sage dể giải đa thức này là dc.

Để tìm hiểu rõ hơn về cách tấn công này có thể lên wu cua anh Tuệ đã viết.


```py
# FLAG = b"crypto{???????????????????????????????????}"

from Crypto.Util.number import *

n = 95341235345618011251857577682324351171197688101180707030749869409235726634345899397258784261937590128088284421816891826202978052640992678267974129629670862991769812330793126662251062120518795878693122854189330426777286315442926939843468730196970939951374889986320771714519309125434348512571864406646232154103
e = 3
c = 63476139027102349822147098087901756023488558030079225358836870725611623045683759473454129221778690683914555720975250395929721681009556415292257804239149809875424000027362678341633901036035522299395660255954384685936351041718040558055860508481512479599089561391846007771856837130233678763953257086620228436828


def pad100(msg):
    return msg + b'\x00' * (100 - len(msg))

flag = b"crypto{" + b"\x00" * len("???????????????????????????????????") + b"}"
print(len(flag))
flag = pad100(flag)

m = bytes_to_long(flag)
print(m)

P.<x> = PolynomialRing(Zmod(n))
f = ((m + (2 **(8 * 58)) * x) ** 3 - c)//(2 ** (8 * 58 * e))

f = f.monic()

print(b"crypto{" + long_to_bytes( int(f.small_roots(epsilon = 1 / 20)[0]) ) + b"}")```


```

### RSA_25

---

**_TASK:_**

Let's Decrypt80 pts · 828 Solves
If you can prove you own CryptoHack.org, then you get access to one of our secrets.

Connect at socket.cryptohack.org 13391

Challenge files:
  - 13391.py

---

Bài này nói chung cũng chỉ là kết nối tới sever nhận file rồi gửi file nên k có j làm khó cả.

```py

from pwn import *
from json import *
from Crypto.Util.number import *

# socket.cryptohack.org 13374

s = connect('socket.cryptohack.org', 13374)

print(s.recv().decode())

dict = {"option": "get_pubkey"}
s.send(dumps(dict).encode())
tmp = loads(s.recv())

N = int(tmp["N"], 16)
e = int(tmp["e"], 16)
dict = {"option": "get_secret"}
s.send(dumps(dict).encode())
tmp = loads(s.recv().decode())
enc = int(tmp["secret"], 16)


print(f"{N = }")
print(f"{e = }")
print(f"{enc = }")


dict = {"option": "sign", "msg": hex(enc)}
s.send(dumps(dict).encode())
tmp = loads(s.recv().decode())
print(long_to_bytes(int(tmp["signature"], 16)))


```


### RSA_27

---

**_TASK:_**

Here's my token signing and verification server. I'm not sure it's doing signing properly, but I've implemented some safeguards to ensure it won't hand out admin tokens to just anyone.

Connect at socket.cryptohack.org 13376

Challenge files:
  - [13376.py](https://cryptohack.org/static/challenges/13376_f33b73edaadf6e553906fb0fc2b79385.py)

---

Bài này cho ta mã hóa bằng d của mọi tin nhắn ta gửi(đương nhiên trừ token :>). Vậy nên mình nhân vào token một số rồi chia lại cho nó là ta sẽ có flag ban đàu và qua mặt dc source, để dễ hiểu thì nó như sau:
$$m ^ d = c \pmod{n}$$
$$(80 * m) ^ {d} \equiv c_1$$
$$(80 ) ^ {d} \equiv c_2$$
$$\to c_1 / c_2 = (80 * m) ^ d / 80 ^ d = (80 / 80 * m) ^ d = m ^ d \pmod{n}$$
từ đó ta có c nên chỉ cần gửi nữa là xong :).
```py

from pwn import *
from json import *
from Crypto.Util.number import *

# socket.cryptohack.org 13376

s = connect("socket.cryptohack.org", "13376")
print(s.recv().decode())

def get_publickey() -> tuple:
    tmp = {"option":"get_pubkey"}
    s.send(dumps(tmp).encode())
    a = loads(s.recv())
    return int(a["N"], 16), int(a["e"], 16)

def send_msg(msg: str) -> str:
    tmp = {"option":"sign", "msg" : str(hex(bytes_to_long(msg))[2:])}

    s.send(dumps(tmp).encode())
    a = loads(s.recv())
    return  int(a["signature"], 16)

def check(msg: str, signature):
    tmp = {"option" : "verify", "msg" : str(hex(bytes_to_long(msg))[2:]), "signature" : signature}
    
    s.send(dumps(tmp).encode())
    a = loads(s.recv())
    return a

msg = b"admin=True"
N, e = get_publickey()

enc_1 = send_msg(long_to_bytes(bytes_to_long(b"admin=True") * 80))
enc_2 = send_msg(long_to_bytes(80))

enc = pow(enc_1 * pow(enc_2, -1, N), 1, N)

print(check(b"admin=True", hex(enc)))



```

## PART_4. More write up

### Crypto_AES

----

**_TASK:_**

```python
import random
import time
import datetime  
import base64
from Crypto.Cipher import AES
flag = b"find_me"
iv = b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"

for i in range(0, 16-(len(flag) % 16)):
    flag += b"\0"

ts = time.time()

print("Flag Encrypted on %s" % datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M'))
seed = round(ts*1000)

random.seed(seed)

key = []
for i in range(0,16):
    key.append(random.randint(0,255))

key = bytearray(key)


cipher = AES.new(key, AES.MODE_CBC, iv) 
ciphertext = cipher.encrypt(flag)

enc = base64.b64encode(ciphertext).decode('utf-8')
print(enc)


# Flag Encrypted on 2023-08-02 10:27
# lQbbaZbwTCzzy73Q+0sRVViU27WrwvGoOzPv66lpqOWQLSXF9M8n24PE5y4K2T6Y

**_Hint:_**
+ Thời gian ở sever và máy tính có thể khác nhau
```

----

Bài này cx khá đơn giản, vì các số random không thật sự ngẫu nhiên mà nó chỉ lấy đầu vào là các số ngẫu nhiên rồi biến đổi nó nên cái mình cần là seed. Khi có seed rồi thì các số dược tạo nên key cũng sẽ hoàn toàn xác định và từ đó ta có thể có cờ.

Solution:
```py
import random
import time
import datetime  
import base64
from Crypto.Cipher import AES

for x in range(0, 24):
    date = "2023-08-02 "+ str(x) + ":27"
    tim = time.strptime(date,'%Y-%m-%d %H:%M')
    l = round(time.mktime(tim)*1000)

    flag = "lQbbaZbwTCzzy73Q+0sRVViU27WrwvGoOzPv66lpqOWQLSXF9M8n24PE5y4K2T6Y"
    flag = base64.b64decode(flag)
    print(flag)
    for i in range(l, l + 60000):

        random.seed(i)
        iv = b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"

        key = []
        for i in range(0,16):
            key.append(random.randint(0,255))

        key = bytearray(key)


        cipher = AES.new(key, AES.MODE_CBC, iv) 
        ciphertext = cipher.decrypt(flag)

        try:
            print(ciphertext.decode('utf-8'))
        except:
            pass

```

### Crpyto


---
**_TAKS:_**

```py
from Crypto.Util.number import*
from Crypto.Cipher import AES
import os
from flag import FLAG

def pad(data):
    padding_size = (16 - (len(data) % 16)) % 16    
    padded_data = data.ljust(len(data) + padding_size, b'\x00')
    return padded_data

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p*q
d = getRandomInteger(512)
key = long_to_bytes(2024*p + d)[:16]
iv = os.urandom(16)
flag = pad(FLAG)
cipher = AES.new(iv,AES.MODE_CBC,key)
c = bytes_to_long(cipher.encrypt(flag))

val = (2*p**3 + 3*p**2 + 2023*d + 2024) % n
assert GCD(val,p) == 1
print('p=' + str(p))
print('n=' + str(n))
print('iv='+str(iv))
print('c=' + str(c))
print('val=' + str(val))
```

---

Bài này mình chỉ cần giải phương trình $val = (2* p ^ 3 + 3 * p ^ 2 + 2023 * d + 2024) \pmod{n}$ là xong. Do đã có p, n, val nên ta chỉ cần chuyểchuyển vế tính toán là ra d, từ đó giải quyết bài toán.

```py
p=9624668906109850998483974056209525089702287918278921274319270522663662804972324391632777024000004445164835957501662407824761862187844902070989943858387023
n=119053833302549126121861824048325871200548851427704067582944667279846987236859718352655950344342118140607658877566141982226231805992080158529128384913766088413693835384148628239859123212444209064815790714735486911276979922175151535850877563374733318947140961515365118979375903413583275044196981685652967357829
iv=b'A-W\x99\xfb.L\x9fG\xe1+\xbd\xb7$\xc9W'
c=36936358040550261245517244362629450151125073316304503047163983542991113186968309568508064867910142605654621794306028
val=15828457744456062568146561470704502856519551484048932569860646681724144906746142293423313013087062265040452331977947251485877654672141881179956278202994177828979975673529189928824770982861399794372799453399059273481330818247215001443788678911988701461334865986451514168580217214527167131248833111697944506238

from Crypto.Util.number import *
from Crypto.Cipher import AES
"""  """
d = pow(pow(val - 2 * p ** 3 - 3 * p ** 2 - 2024, 1, n) * pow(2023, -1, n), 1, n)
key = long_to_bytes(2024 * p + d)[:16]
cipher = AES.new(iv, AES.MODE_CBC, key)
flag = cipher.decrypt(long_to_bytes(c))
print(flag )



```


### Crypto

---

**_TASK:_**



```python

from Crypto.Util.number import *
from Crypto.Cipher import AES
import os
from flag import FLAG

def pad(data):
    padding_size = (16 - (len(data) % 16)) % 16    
    padded_data = data.ljust(len(data) + padding_size, b'\x00')
    return padded_data

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p*q
d = getRandomInteger(64)
key = long_to_bytes(2024*p + d)[:16]
iv = os.urandom(16)
flag = pad(FLAG)
cipher = AES.new(iv,AES.MODE_CBC,key)
c = bytes_to_long(cipher.encrypt(flag))

val = (2*p**3 + 3*p**2) % n

print('n=' + str(n))
print('iv='+str(iv))
print('c=' + str(c))
print('val=' + str(val))

```
---

Ở đây ta dễ thấy $val \equiv 2 * p ^ 3 + 3 * p ^ 2 \pmod{n} \quad \to \quad val = p ^2 * (2 * p + 3) \pmod{n}$, mà $n = p * q$ nên từ đó ta có $gcd(val, n) = p$. Do $2024 * p >> random(64)$ mà key chỉ lấy có 16 bytes đầu của nó nên ở đây d trở nên vô dụng, từ đó ta dễ dàng có được key và hoàn thành thử thách.

```
n=116422885145248934225686914429146707250914314074098936204837356406828626206897073267773920624624570359557096258952933379700970822531971353624244003807545840017125763493920463202691952331937661437791742467140169441129657049404630272768006776625873529380414431191459118716479168976156074571723572848577917978433
iv=b':\x88(\x7fPK\xba+\x83G\xd9+\xb4:w\x02'
c=26003470241248183886366385521067853859993513649868770030402657395420294707645314821746877611126190234881774517848630
val=7728896068211597749662327611345565126580093002981776126298758158041181358825984746690714615330702804921437965445589537359948914406962280207495027174049984054166471642458821726259288576073467035129599467101913206457949501633692562613026832767483110632244571322446440661984724942084414921153978748727244489994

p = GCD(val,n)
key  = long_to_bytes(2024*p)[:16]
cipher = AES.new(iv,AES.MODE_CBC,key)
flag = cipher.decrypt(long_to_bytes(c))
print(flag)
```


### Crypto

---

**_TASK:_**
```py
from Crypto.Util.number import getPrime , bytes_to_long , GCD
import random
import time
import os
import json


random.seed(time.time())

flag = b'KCSC{T0o_much_t1mE_to_So1ve_T.T}' 

KEY_SIZE = 512
e = 65537
banner = 'RSA, or Rivest_Shamir_Adleman, is a widely-used public-key cryptosystem for secure communication. Can you break it ?'
print(banner)

def fast_exp(a, b, n):
    output = 1
    while b > 0:
        if b & 1:
            output = output * a % n
        a = a * a % n
        b >>= 1 
    return output    
def check(p, q, n):
    a_ = random.randint(1, 100)
    b_ = random.randint(1, 100)
    s = fast_exp(p, fast_exp(q, a_, (p - 1) * (q - 1)), n)
    t = fast_exp(q, fast_exp(p, b_, (p - 1) * (q - 1)), n)
    hint = s + t
    print(f'{hint = }')
def gen_RSA_params(N, e):
    p = getPrime(N)
    q = getPrime(N)
    while GCD(e, (p - 1) * (q - 1)) > 1:
        p = getPrime(N)
        q = getPrime(N)
    n = p * q
    check(p, q, n) 
    return (p, q, n)
p, q, n = gen_RSA_params(KEY_SIZE, e)

if __name__ == "__main__":
    print("Choose your option: ")
    print("1 : Get_Public_Key")
    print("2 : Get_ciphertext")
    print("3 : Check")
    while True:
     idx = json.loads(input())
     if idx['option'] == 'Get_Public_Key' :
      print(f'{n = }')
      print(f'{e = }')
     if idx['option'] == 'Get_ciphertext' :
      m = bytes_to_long(os.urandom(128))
      c = pow(m,e,n)
      print(f'ciphertext : {c}')
     if idx['option'] == 'check' :
      d = int(idx['private_key'],16)
      if pow(c,d,n) == m :
          print(f'Here is your flag : {flag}')
          break
      else :
          print('bruh')
```

---

$\to$ Dễ thấy hàm fast_exp(a, b, n) = $a ^ b \pmod{n}$. Từ đó ta có hàm check sẽ tương đương như sau:
$$\text{fast exp}(q, a, (p - 1) * (q - 1)) =  q ^ a \pmod{phi} \quad = \quad q ^ a + k * phi, \forall k \in R$$
$$\text{fast exp}(p, \text{fast exp}(q, a, (p - 1) * (q - 1)), n) = q ^ {p ^ a + k * phi} \pmod{n} = q ^ {p ^ a} \pmod{n}$$

mà ta có:


$$
\begin{cases}
  p ^ {q ^ a}  \equiv 0 \equiv p \pmod{p} \\
  p ^ {q ^ a}  \equiv p \pmod{q}
\end{cases}
$$

$$\to p ^ {q ^ a} = p \pmod{n}$$

Chứng minh cái còn lại tương tự, từ đó ta thấy hint = p + q. Nên phi = n - hint + 1

```python

from pwn import *
from json import *
from Crypto.Util.number import *
import random
import time
import os
import json
from tqdm import *
from factordb.factordb import FactorDB
from gmpy2 import iroot

s = process(["python3", "t.py"])



print(s.recvuntil(b"hint = ").decode())
total = int(s.recvline().decode())
print(s.recvuntil(b"3 : Check\n").decode())

dict = {"option":"Get_Public_Key"}
s.sendline(dumps(dict).encode())
s.recvuntil(b"n = ")
n = int(s.recvline().decode())
dict = {"option":"Get_ciphertext"}
s.sendline(dumps(dict).encode())

s.recvuntil(b"ciphertext : ")
cipher = int(s.recvline().decode())
KEY_SIZE = 512
e = 65537
print(f"e : {e}")
print(f"n : {n}")
print(f"cipher : {cipher}")
print(f"key_size : {KEY_SIZE}")

# x ^ 2 - total * x + n = 0
delta = total * total - 4 * n
p = (total + iroot(delta, 2)[0]) // 2
q = n //p
phi = (p-1)*(q-1)
s.sendline(dumps({"option" : "check", "private_key" : hex(pow(e, -1, phi))}).encode())
tmp = s.recv()
if b"flag" in tmp:
    print(tmp)

```

### Crypto_RSA_Lmao

---

**_TASK:_**
```
n = b'MHgzMDE5NzgzNTMzYjljZWVhNDA5YjkzM2QwMjdlZjMyZTFjYWYwZjE2OWIzYzcwNTVlZTM0Njk1MDA4NGFlN2I2YzU3NGNjN2I4ZmY1Mjc0Nw=='

e = '0x61327'

c = b'MHgxNjdkYTJiMzhhYmRiYjg4N2FmZmM0MDlkNGQzNGQxOTdhMDJmNjJhY2E0YTFjNWM4MTk3YjlhZjlkZWU1NDViNTQ5YjBmNWI3NjI0ZjUzNw=='
```
**_Hint:_**

+ $p - 1 \equiv 0 \pmod{e}$
+ [crypto.stack](https://crypto.stackexchange.com/questions/81949/how-to-compute-m-value-from-rsa-if-phin-is-not-relative-prime-with-the-e/81966#81966)

---

Có $n$ là prime mà $n - 1 \equiv 0 \pmod{e} \quad \to \quad phi = k * e$ nên ta không thể tính $d$. Thay vào đó ta sẽ tính m như sau:
Then, one way to derive the possible plaintexts is to compute:

$$C ^ {d} * L ^ {i} \mod{n}$$

where:

+ $λ = (p − 1) * (q − 1) / gcd(p − 1, q − 1)$
+ $C$ is the ciphertext
+ $d \equiv e^{−1} \pmod{λ/e}$. (This is well defined, as $λ/e$ is an integer which is relatively prime to $e$)
+ $L \equiv k ^ {λ/e} \pmod{n}$ where k is an integer such that L≠1(and any such value L works); most values of kwork
+ $i$ is any integer $0 \leq i < e$

Nhưng do ở đây $n$ là prime nên $\lambda = phi(n) = n - 1$


```python


from Crypto.Util.number import *
from base64 import *
from tqdm import *

n = b'MHgzMDE5NzgzNTMzYjljZWVhNDA5YjkzM2QwMjdlZjMyZTFjYWYwZjE2OWIzYzcwNTVlZTM0Njk1MDA4NGFlN2I2YzU3NGNjN2I4ZmY1Mjc0Nw=='
e = '0x61327'
c = b'MHgxNjdkYTJiMzhhYmRiYjg4N2FmZmM0MDlkNGQzNGQxOTdhMDJmNjJhY2E0YTFjNWM4MTk3YjlhZjlkZWU1NDViNTQ5YjBmNWI3NjI0ZjUzNw=='

n = int(b64decode(n).decode(), 16)
e = int(e, 16)
c = int(b64decode(c).decode(), 16)

lam  = (n - 1)
d = pow(e, -1, lam // e)
l = pow(2, lam // e, n)

for x in tqdm(range(0, e), desc = "Progress"):

    flag = long_to_bytes((pow(c, d, n) * pow(l, x, n)) % n)
    if b"KCSC" in flag :
        print(flag)
        break




```

### Crypto


```py
from Crypto.Util.number import*
from Crypto.Cipher import AES
import os
from flag import FLAG

def pad(data):
    padding_size = (16 - (len(data) % 16)) % 16    
    padded_data = data.ljust(len(data) + padding_size, b'\x00')
    return padded_data

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p*q
assert n**0.4 <p < n**0.5 and n**0.5 <q < n**0.6 
random = getRandomInteger(64)
d = p**2 + 2023*p + random 
key = long_to_bytes(2024*p + d)[:16]
iv = os.urandom(16)
flag = pad(FLAG)
cipher = AES.new(iv,AES.MODE_CBC,key)
c = bytes_to_long(cipher.encrypt(flag))
val = (2*d**3 + 3*d**2 + pow(2024,2023,n)*d + pow(2023,2024,n)) % n
assert GCD(val,p) == 1
print('n=' + str(n))
print('iv='+str(iv))
print('c=' + str(c))
print('val=' + str(val))
n=142999029343358149662443097604976747149889090072418385001202757765412807102794121676470074077745347521711600216686223755592471644777386772752828715272883803776637467307260243598922717717430378428346324530435952902140546517524282746208308333525505122994592661438040867038101159049208880230622261413767942142899
iv=b'K\xf3\xa1*e\xbf-<\x1d\xfd\x91Y0T\x8cC'
c=35260492240097997303991122370438160834896641282850629162240901531615420795101121531531378708194860237459245665887783
val=70156641495735636837250712165710253952947005832933959682127322686854887620192055132242994711727701574635292973129375275947527025543419041137384040724483962599342431159651204942389005208600195434478927233540663125221124326257296063411788927862801717458400080626132989001264778380940137062679553487367937251196
```

haizz viết rồi nhưng bị mất nên k viết nx.
```py

from Crypto.Util.number import*
from Crypto.Cipher import AES
import os
from Crypto.Util.number import bytes_to_long, getRandomNBitInteger
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

n=142999029343358149662443097604976747149889090072418385001202757765412807102794121676470074077745347521711600216686223755592471644777386772752828715272883803776637467307260243598922717717430378428346324530435952902140546517524282746208308333525505122994592661438040867038101159049208880230622261413767942142899
iv=b'K\xf3\xa1*e\xbf-<\x1d\xfd\x91Y0T\x8cC'
c=35260492240097997303991122370438160834896641282850629162240901531615420795101121531531378708194860237459245665887783
val=70156641495735636837250712165710253952947005832933959682127322686854887620192055132242994711727701574635292973129375275947527025543419041137384040724483962599342431159651204942389005208600195434478927233540663125221124326257296063411788927862801717458400080626132989001264778380940137062679553487367937251196

"""
delta = getRandomNBitInteger(64)
x = p**2 + 1337*p + delta

val = (pow(2,e,n)*(x**3) + pow(3,e,n)*(x**2) + pow(5,e,n)*x + pow(7,e,n)) % n
"""

def small_roots(f, X, beta=1.0, m=None):
    N = f.parent().characteristic()
    delta = f.degree()
    if m is None:
        epsilon = RR(beta^2/f.degree() - log(2*X, N))
        m = max(beta**2/(delta * epsilon), 7*beta/delta).ceil()
    t = int((delta*m*(1/beta - 1)).floor())
    print(f"m = {m}")
    
    f = f.monic().change_ring(ZZ)
    P,(x,) = f.parent().objgens()
    g  = [x**j * N**(m-i) * f**i for i in range(m) for j in range(delta)]
    g.extend([x**i * f**m for i in range(t)]) 
    B = Matrix(ZZ, len(g), delta*m + max(delta,t))

    for i in range(B.nrows()):
        for j in range(g[i].degree()+1):
            B[i,j] = g[i][j]*X**j

    B =  B.LLL()
    f = sum([ZZ(B[0,i]//X**i)*x**i for i in range(B.ncols())])
    roots = set([f.base_ring()(r) for r,m in f.roots() if abs(r) <= X])
    return [root for root in roots if N.gcd(ZZ(f(root))) >= N**beta]

PR.<d> = PolynomialRing(Zmod(n))

f = (2*d**3 + 3*d**2 + pow(2024,2023,n)*d + pow(2023,2024,n)) - val

f = f.monic()

random = small_roots(f, beta = 0.1, X = 2 ** 64, m = 3)[0]

p = int(gcd(int(f(random)), n))
q = n // p

d = p**2 + 2023*p + random 
key = long_to_bytes(2024*p + d)[:16]

cipher = AES.new(iv,AES.MODE_CBC,key)
c = (cipher.decrypt(long_to_bytes(c)))
print(c)
```

### I don't know What is this.



---

**_TASK:_**

```py

from Crypto.Util.number import *
import random
from gmpy2 import *
def get_prime(bits) :
    while True :
     p = 2
     while p.bit_length() < bits :
        p*= getPrime(8) 
     if isPrime(p+1) :
         return p+1      
flag = b'KCSC{?????????????}'
p = get_prime(512)
q = get_prime(512)
n = p*q
print(f'{n = }')
print(f'c = {pow(3,bytes_to_long(flag),n)}')
#n = 1174556662732377729753746846255900491704955961343461200080564199322237885581603926726516997712720433122082565645974057007596744198270193643980828638834556474415306371445913593102376102319076454903159175634642944543400716516498090102283852532059453599194173184765786904663505978986631763459552108833366974132009
#c = 152993281732457298849631014922688377344907716267851006077475374500755000779427508706498957223115264888063631538343997010934492882463398402705977958681603317390229041985915114607651463371095431210572041531191689927973785121861082427609044041691046590353776520215625148229399932355060848445113826274866051892104
```

---

🥇

[information](https://juejin.cn/post/7148772467194986504)

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/c396945c-dd64-4878-b6cd-5288f7b3b462)

Đẻ giải thích dễ hiểu hơn thì ta có:

+ Theo định lý Fermat nhỏ ta có : $a ^ {p - 1} = 1 \pmod{p} \forall { \text {p is prime}}$
+ gọi $a$ là tích của các prime mà p, q có thể có (ở trong bài này là khoảng [2: $2 ^ 8$]) từ đó ta có $a = k_1 * p = k_2 * q$

Từ đó $2 ^ a = 2 ^ {k_1 * p} = { 2 ^ p} ^ {k_1} = 1 ^ {k_1} \pmod{p}$ nên $2 ^ a - 1 = k * p$

Từ đó: gcd(2 ^ a - 1, n) = gcd(k * p, p * q) = p.

từ đó ta dễ dàng có được p. rồi sử dụng p để tính discrete_log trong mod p là được (vì p là smooth prime và tính trong mod p hay n cũng tương đương)

```py

n = 1174556662732377729753746846255900491704955961343461200080564199322237885581603926726516997712720433122082565645974057007596744198270193643980828638834556474415306371445913593102376102319076454903159175634642944543400716516498090102283852532059453599194173184765786904663505978986631763459552108833366974132009
c = 152993281732457298849631014922688377344907716267851006077475374500755000779427508706498957223115264888063631538343997010934492882463398402705977958681603317390229041985915114607651463371095431210572041531191689927973785121861082427609044041691046590353776520215625148229399932355060848445113826274866051892104

from sympy.ntheory.residue_ntheory import discrete_log
import gmpy2
from Crypto.Util.number import *

prd = 1
for x in range(256):
    if isPrime(x):
        prd *= x

p = gmpy2.gcd(gmpy2.powmod(2,prd ** 5,n) - 1,n)

q = n // p

print(long_to_bytes(discrete_log(p, c, 3)))


```
