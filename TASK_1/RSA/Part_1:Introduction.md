
1. Tổng quan

Mã RSA, được phát minh bởi Rivest, Shamir, Adleman. Sử dụng toán học làm nền tảng, đã nhiều lần bị tấn công nhưng nó vẫn chưa thực hiện được. 

Đặt $n = p * q$ với p, q là hai số nguyên tố lớn có cùng kích thước ($n / 2$ bít). Yêu cầu thấp nhất để được coi là an toàn thì n phải có ít nhất 1024 bit. Lấy e, d sao cho $ed = 1 (\mod{phi} )$,  với $phi = (q - 1)*(p -1)$ trong nhóm $Z_{n}$. Gọi $n$ là module của RSA, e là mã khóa, d là giải mã. Cặp $(N, e)$ là public key, $(N, d)$ là private key.

Một tin nhắn là một số tự nhiên m thuộc nhóm $Z_{n}$. Để mã hóa m, ta cần tính $c = m^e \mod N$. Để giải mã c, ta cần tính $m = c^d \mod N$. Thật vậy:

  + Theo định lý nhỏ Fermat : $c^d = m^d*m^e = m\mod N$

Nếu d được cho việc tính toán m trở nên rất dễ ràng, Khi muốn biết d từ n thì nó trở thành một bài toán khó còn được gọi là trap_door. Khi muốn phá RSA, có $(N, e, C)$, rất khó để tính được $\sqrt[e]{C} \mod N$. Vì nhóm hữu hạn $Z_n$ lớn nên rất khó để tìm $d$ sao cho $M$ đúng. Trong RSA hàm $x \to x^e \mod N$ là một ví dụ cho bẫy sập một chiều. Rễ dàng để tính, nhưng khó để đảo ngược.

2. factoring large intergers
 +  Tấn công vào public key đơn giản nhất đó chính là phân tích nhân tử cho n từ đó có thể dễ dàng tìm được phi n thông qua $ed = 1 (\mod phi)$. (Được gọi là tấn công bạo lực :v). Nhưng việc phân tích nhân tử một số lớn là một trong những bài toán khó tốn nhiều thời gian từ đó việc tấn công này chở nên bất khả thi về mặt thời gian.
 +  Ngòai ra, khi biết $d$ và $e$ thì ta có thể tìm được $n$ từ đó tìm được $(q, p)$.


   
