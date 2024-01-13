
1. Common modulus
   
   Để tránh tạo ra một modulo nhiều lần cho mọi người thì việc tạo ra một mod cho nhiều người dùng thoạt nhìn thì có thể vẫn an toàn(dùng chung một N cho nhiều người dùng và có các hệ số e, d khác nhau).
   Nếu chúng ta biết e_a, d_a thì thì ta hoàn toàn tim ra dc q, p của N. Từ đó với e_b của một người bất kỳ nào đó thit ta sẽ tính ra dc d_b đó và từ đó có thể dễ dàng mã hóa được c_b.

2. Blinding
   
   Với (N, e) là khóa chung, (N, d) là khóa chung. với  là tin nhắn chưa được mã hóa, chọn một số r thuộc Zn* lấy M' = rM. Từ đó mã hóa M', => S = M'^e = r^e * M^e (mod N). Từ đó, M = M'/e^r (mod N)
    Kỹ thuật này bình thường thì k quan trọng, nhưng nó khá có ích trong việc ẩn danh.
3. Low private exponent
   
   Khi e quá nhỏ thì dẫn tới việc d bị quá lớn từ đó dẫn tới việc giải mã bị tốn nhiều thời gian. Để k bị tốn nhiều thời gian thì cho e lớn, dẫn tới việc d nhỏ hơn và giảm thời gian mã hóa. Nhưng nếu d quá nhỏ sẽ dẫn tới trường hợp khóa yếu từ đó dễ bị tấn công.Khi d < (1/3)d^(1/4), q < p < 2q, ta có thể tấn công như sau:
   + ed = 1 (mod phi) => ed = 1 + k*phi => e/phi - k/d = 1/(d * phi) vì 1/(d * phi) rất nhỏ nên từ đó ta có thể suy ra e/phi = k/d
   + phi = (q - 1)*(p - 1) => phi = N - q - p +1 => p + q -1 = 1/3 (n^(1/2)) nên |N - phi| = 1/3 (n^(1/2))

   => thay n vào phi ta có: e/N - k/d = (ed - k*N)/(N * d) = (ed - kphi + k*N + k*phi) < 1/2(N^2)

   Từ đó sử dụng tính chất của phân số, ta có thể dễ dàng tính được k/d (:v dell hiểu j). Từ đó ta tìm dc d. từ d và e ta có thể dễ dàng tính phi.
   

