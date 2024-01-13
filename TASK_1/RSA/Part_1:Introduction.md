### PART_1

1. Tổng quan

Mã RSA, được phát minh bởi Rivest, Shamir, Adleman. Sử dụng toán học làm nền tảng, đã nhiều lần bị tấn công nhưng nó vẫn chưa thực hiện được. 

Đặt $n = p * q$ với p, q là hai số nguyên tố lớn có cùng kích thước ($n / 2$ bít). Yêu cầu thấp nhất để được coi là an toàn thì n phải có ít nhất 1024 bit. Lấy e, d sao cho $ed = 1 (\mod{phi} )$,  với $phi = (q - 1)*(p -1)$ trong nhóm $Z_{n}$. Gọi $n$ là module của RSA, e là mã khóa, d là giải mã. Cặp $(N, e)$ là public key, $(N, d)$ là private key.

Một tin nhắn là một số tự nhiên m thuộc nhóm $Z_{n}$. Để mã hóa m, ta cần tính $c = m^e \mod N$. Để giải mã c, ta cần tính $m = c^d \mod N$. Thật vậy:

  + Theo định lý nhỏ Fermat : $c^d = m^d*m^e = m\mod N$

Nếu d được cho việc tính toán m trở nên rất dễ ràng, Khi muốn biết d từ n thì nó trở thành một bài toán khó còn được gọi là trap_door. Khi muốn phá RSA, có $(N, e, C)$, rất khó để tính được $\sqrt[e]{C} \mod N$. Vì nhóm hữu hạn $Z_n$ lớn nên rất khó để tìm $d$ sao cho $M$ đúng. Trong RSA hàm $x \to x^e \mod N$ là một ví dụ cho bẫy sập một chiều. Rễ dàng để tính, nhưng khó để đảo ngược.

2. factoring large intergers
 +  Tấn công vào public key đơn giản nhất đó chính là phân tích nhân tử cho n từ đó có thể dễ dàng tìm được phi n thông qua $ed = 1 (\mod phi)$. (Được gọi là tấn công bạo lực :v). Nhưng việc phân tích nhân tử một số lớn là một trong những bài toán khó tốn nhiều thời gian từ đó việc tấn công này chở nên bất khả thi về mặt thời gian.
 +  Ngòai ra, khi biết $d$ và $e$ thì ta có thể tìm được $n$ từ đó tìm được $(q, p)$.

### PART_2


1. Common modulus
   
   Để tránh tạo ra một modulo nhiều lần cho mọi người thì việc tạo ra một mod cho nhiều người dùng thoạt nhìn thì có thể vẫn an toàn(dùng chung một $N$ cho nhiều người dùng và có các hệ số $e, d$ khác nhau).
   Nếu chúng ta biết $e_a, d_a$ thì thì ta hoàn toàn tim ra dc $q, p$ của $N$. Từ đó với $e_b$ của một người bất kỳ nào đó thì ta sẽ tính ra dc $d_b$ đó và từ đó có thể dễ dàng mã hóa được $c_b$.

2. Blinding
   
   Với $(N, e)$ là khóa chung, $(N, d)$ là khóa chung. với M là tin nhắn chưa được mã hóa, chọn một số r thuộc $Z_n^*$ lấy $M' = r * M$. Từ đó mã hóa M', $S = M'^e = r^e * M^e (\mod N)$. Từ đó, $M = M'/e^r (\mod N)$
    Kỹ thuật này bình thường thì không quan trọng, nhưng nó khá có ích trong việc ẩn danh.
3. Low private exponent
   
   Khi $e$ quá nhỏ thì dẫn tới việc d bị quá lớn từ đó dẫn tới việc giải mã bị tốn nhiều thời gian. Để không bị tốn nhiều thời gian thì cho $e$ lớn, dẫn tới việc $d$ nhỏ hơn và giảm thời gian mã hóa. Nhưng nếu $d$ quá nhỏ sẽ dẫn tới trường hợp khóa yếu từ đó dễ bị tấn công.Khi $d < \sqrt[4]{N} / 3,  q < p < 2 * q$, ta có thể tấn công như sau:
   + $e*d = 1 (\mod phi)$ $\to$ $ed = 1 + k*phi$ $\to$ $e/phi - k/d = 1/(d * phi)$ vì $1/(d * phi)$ rất nhỏ nên từ đó ta có thể suy ra e/phi = k/d
   + phi = (q - 1)*(p - 1) => phi = N - q - p +1 => p + q -1 = 1/3 (n^(1/2)) nên |N - phi| = 1/3 (n^(1/2))

   => thay n vào phi ta có: e/N - k/d = (ed - k*N)/(N * d) = (ed - kphi + k*N + k*phi) < 1/2(N^2)

   Từ đó sử dụng tính chất của phân số, ta có thể dễ dàng tính được k/d (:v dell hiểu j). Từ đó ta tìm dc d. từ d và e ta có thể dễ dàng tính phi.

   Để tránh trường hợp bị tấn công wiener đã đưa ra 2 cách bảo vệ như sau:
      + đặt e' = e + k * phi, sao cho e' > n ^(1.5) khi đó ta khồn thể tấn công với cả d rất nhỏ.
      + Sử dụng d lớn và giải mã bằng CRT. Tìm d_p, d_q rồi dùng CRT để tính m dựa vào hệ m_p = c^(d_p) (mod p) và m_q = c^(d_q) (mod q)
        . Từ đó m = m_p (mod p), m = m_q (mod q)

        
   


   
