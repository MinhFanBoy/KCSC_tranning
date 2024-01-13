1. Timing attack
   Đây là kiểu tấn công đươn giản và rất không hiệu quả nên không được sử dụng trong thực tế.

   Viết d dưới dạng nhị phân ta có: d = d0d1...dn nên d = sigma(2^i * di) với i từ 0 đến n.
   Từ đó, đặt z = M, c = 1 for i = 0, ..., n
   + if: d_i = 1 thì c = c*z (mod N)
   + else: z = z ^ 2 (mod N)
   => cuối dùng C = M ^ d (mod N)

    Vì d là số lẻ nên d_0 luôn bằng 1, Ở lần lặp tiếp theo vì có sự khác biệt giữa thời gian thực hiện phép tính nên ta có thể xác định lần lượt các d_i tiếp theo. Cứ tiếp tục như vậy để khôi phục d. Lưu ý khi số e nhỏ dược sử dụng ta chỉ cần khôi phục 1/4 số bít của d.

2. random fault
   Trong RSA, việc giải mã có thể sử dụng CRT để giảm thời gian chạy. Thay vì hoạt động trên modulus N thì ta chỉ hoạt động trên q, p từ đó giúp giảm thời gian.

   + c_p = M^(d_p) (mod p) và c_q = M^(d_q) (mod q)
   + với d_p = d mod(p - 1), d_q = d (mod q - 1)
   + c = a * c_p + b * c_q (mod N)

   Trong một vài trường hợp có thể sảy ra lỗi như sau: c_q ^ e = M (mod p) but c_p ^ e != M (mod p). Từ đó, gcd(N, c_p ^ e) = p. Để kiểu tấn công này hoạt động, ta cần phải biết M. Nên yêu cầu M phải là văn bản thuần k dc pad.

3. PKCS1 attack

   Với N có n bits RSA và tin nhắn mã hóa có m bits mà m < n thì trước khi được mã hóa tin nhắn thường được pad thêm sao cho m' = n. Tiêu chuẩn thường dược sử dụng để pad là PKCS1, nó có dạng:
   + "02" + random + 00 + M
     
   Khi tin nhắn được giải mã nó sẽ phải kiểm tra xem có "02" ở trong không. Nếu như không có nó sẽ gửi về lỗi nên từ đó ta sẽ biết được tin nhắn có dc pad hay k và có thể tấn công nó. Chọn một số ngẫu nhiên r < Zn, tính toán C' = c * r (mod N) gửi C' đi mã hóa. Từ đó có thể giải mã C. 
    
