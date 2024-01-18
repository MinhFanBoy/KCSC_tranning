
# Tables of contens:
[PART_1: Giới thiệu chung]()
+ [Tổng quan]()
+ [Bài toán phân tích thừa số]()

[PART_2: Attack]()
+ [1. Common modulus](###1.Common-modulus)
+ [2. Blinding](### 2. Blinding)
+ [3. Low private exponent]()
+ [4. Hastad's attack]()
+ [5. Fermat's attack]()
+ [6. Timing attack]()
+ [7. random fault]()
+ [8. PKCS1 attack]()

## PART_1: Giới thiệu chung

### 1. Tổng quan

Mã RSA, được phát minh bởi Rivest, Shamir, Adleman. Sử dụng toán học làm nền tảng, đã nhiều lần bị tấn công nhưng nó vẫn chưa thực hiện được. 

Đặt $n = p * q$ với p, q là hai số nguyên tố lớn có cùng kích thước ($n / 2$ bít). Yêu cầu thấp nhất để được coi là an toàn thì n phải có ít nhất 1024 bit. Lấy e, d sao cho $ed = 1 (\mod{phi} )$,  với $phi = (q - 1)*(p -1)$ trong nhóm $Z_{n}$. Gọi $n$ là module của RSA, e là mã khóa, d là giải mã. Cặp $(N, e)$ là public key, $(N, d)$ là private key.

Một tin nhắn là một số tự nhiên m thuộc nhóm $Z_{n}$. Để mã hóa m, ta cần tính $c = m^e \mod N$. Để giải mã c, ta cần tính $m = c^d \mod N$. Thật vậy:

  + Theo định lý nhỏ Fermat : $c^d = m^d*m^e = m\mod N$

Nếu d được cho việc tính toán m trở nên rất dễ ràng, Khi muốn biết d từ n thì nó trở thành một bài toán khó còn được gọi là trap_door. Khi muốn phá RSA, có $(N, e, C)$, rất khó để tính được $\sqrt[e]{C} \mod N$. Vì nhóm hữu hạn $Z_n$ lớn nên rất khó để tìm $d$ sao cho $M$ đúng. Trong RSA hàm $x \to x^e \mod N$ là một ví dụ cho bẫy sập một chiều. Rễ dàng để tính, nhưng khó để đảo ngược.

### 2. factoring large intergers
 +  Tấn công vào public key đơn giản nhất đó chính là phân tích nhân tử cho n từ đó có thể dễ dàng tìm được phi n thông qua $ed = 1 (\mod phi)$. (Được gọi là tấn công bạo lực :v). Nhưng việc phân tích nhân tử một số lớn là một trong những bài toán khó tốn nhiều thời gian từ đó việc tấn công này chở nên bất khả thi về mặt thời gian.
 +  Ngòai ra, khi biết $d$ và $e$ thì ta có thể tìm được $n$ từ đó tìm được $(q, p)$.

## PART_2: Attack


### 1.Common modulus
   
Để tránh tạo ra một modulo nhiều lần cho mọi người thì việc tạo ra một mod cho nhiều người dùng thoạt nhìn thì có thể vẫn an toàn(dùng chung một $N$ cho nhiều người dùng và có các hệ số $e, d$ khác nhau).

Nếu chúng ta biết $e_a, d_a$ thì thì ta hoàn toàn tìm ra dc $q, p$ của $N$. Từ đó với $e_b$ của một người bất kỳ nào đó thì ta sẽ tính ra dc $d_b$ đó và từ đó có thể dễ dàng mã hóa được $c_b$.

Giả sử: $e_a, d_a,N$ đã biết lúc đó ta có:
Tồn tại $k$ sao cho $e_a * d_a = 1 + k * phi$
$$phi = (e_a * d_a - 1)/k \text{   } \forall phi \in N^*$$
Từ đó ta dễ dàng tìm được phi. Và ta cũng có $phi = (p - 1) * (q - 1) \to phi = N - q - p + 1$

Xét phương trình $(x - q) * (x - p) == 0$, dễ thấy pt có hai nghiệm phân biệt là $p, q$. Phương trình tương đương $x^2 - (p + q) * x + p * q = 0$. Kết hợp với phi đã tính ở trên, ta có: $$x^2 - (N - phi + 1) * x + N = 0$$
Từ đó dễ dàng tìm được $p, q$ , để chắc chắn có thể thêm điều kiện $q, p$ là số nguyên tố. Với $phi, e_b$ ta hoàn toàn có thể tính ra $d_b$ rồi từ đó mã hóa tin nhắn.


   

### 2. Blinding
   
   Với $(N, e)$ là khóa chung, $(N, d)$ là khóa chung. với M là tin nhắn chưa được mã hóa, chọn một số r thuộc $Z_n^*$ lấy $M' = r * M$. Từ đó mã hóa M', $S = M'^e = r^e * M^e (\mod N)$. Từ đó, $M = M'/e^r (\mod N)$
    Kỹ thuật này bình thường thì không quan trọng, nhưng nó khá có ích trong việc ẩn danh.
### 3. Low private exponent
   
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

Trong RSA, $q, p$ nên có chung độ dài để có thể tạo nên một khóa mạnh mẽ, nhưng nếu $q, p$ quá gần nhau lại dẫn dến trường hợp khóa yếu dễ bị tấn công.
Giả sử: $N = (a - b) * (a + b) = a^2 - b^2 \quad \forall a, b \in Z^*$
$$b^2 = a^2 - N$$
$$b = \sqrt{a^2 - N}$$

Với $a = \sqrt{N}, b = a^2 - n$ thử lần lượt với mọi $x > a$ sao cho thỏa mãn hệ.Với cách brute force như vậy nên cách tấn công này chỉ áp dụng với các sô q và p gần nhau


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

Với $N$ có $n$ bits RSA và tin nhắn mã hóa có $m$ bits mà $m < n$ thì trước khi được mã hóa tin nhắn thường được pad thêm sao cho $m' = n$. Tiêu chuẩn thường dược sử dụng để pad là PKCS1, nó có dạng:
   + "02" + random + 00 + M
     
Khi tin nhắn được giải mã nó sẽ phải kiểm tra xem có "02" ở trong không. Nếu như không có nó sẽ gửi về lỗi nên từ đó ta sẽ biết được tin nhắn có dc pad hay k và có thể tấn công nó. Chọn một số ngẫu nhiên $r < Z_n$, tính toán $C' = c * r \pmod{N}$ gửi $C'$ đi mã hóa. Từ đó có thể giải mã $C$. 
    



              


   
