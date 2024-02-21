
Tables of contents
==================


## I. Kiến thức cơ bản

### 1. Giới thiệu chung

Lịch sử của mật mã học có thể được chia thành hai thời đại: kỷ nguyên cổ điển và kỷ nguyên hiện đại. Bước ngoặt xảy ra vào năm 1977, khi cả thuật toán RSA và thuật toán trao đổi khóa Diffie-Hellman được giới thiệu. Các thuật toán mới này mang tính cách mạng bởi vì chúng đại diện cho các sơ đồ mã hóa khả thi đầu tiên trong đó bảo mật dựa trên lý thuyết về các con số; đó là lần đầu tiên cho phép liên lạc an toàn giữa hai bên mà không có bí mật chung.

Trong vài thập kỷ gần đây, đường cong elliptic đóng vai trò quan trọng đối với lý thuyết số và mật mã. Mật mã đường cong elliptic (ECC) được giới thiệu lần đầu vào năm 1991 bởi các công trình nghiên cứu độc lập của Neals Koblitz và Victor Miller. Độ an toàn của ECC dựa vào bài toán logarit rời rạc trên nhóm các điểm của đường cong elliptic (ECDLP). Đối với bài toán logarit rời rạc trên trường hữu hạn hoặc bài toán phân tích số, tồn tại các thuật toán dưới dạng dạng hàm mũ để giải các bài toán này (tính chỉ số hoặc sàng trường số). Tuy nhiên, đối với bài toán ECDLP cho đến nay vẫn chưa tìm được thuật toán dưới hàm mũ để giải. Nhà toán học nổi tiếng J. Silverman cũng như nhiều nhà thám mã khác đã nghiên cứu các thuật toán tương tự, như thuật toán tính chỉ số để áp dụng cho ECDLP nhưng đều không thành công. Hiện nay, thuật toán tốt nhất để giải bài toán ECDLP là Pollard với độ phức tạp cỡ, trong đó G là nhóm điểm đường cong elliptic. Điều này đã tạo ra những ưu việt của hệ mật ECC so với các hệ mật khóa công khai khác.

Các hàm logarit rời rạc đường cong elip là vấn đề khó khăn trong việc củng cố mật mã đường cong elliptic. Mặc dù đã có gần ba thập kỷ nghiên cứu, các nhà toán học vẫn chưa tìm thấy một thuật toán để giải quyết vấn đề này nhằm cải thiện cách tiếp cận. Nói cách khác, dựa trên toán học hiện đang hiểu, dường như không có một lối tắt nào thu hẹp khoảng cách trong Hàm Bẫy dựa trên vấn đề này. Điều này có nghĩa là đối với các số có cùng kích thước, việc giải các logarit rời rạc đường cong elip khó khăn hơn. Vì vậy cho ta một hệ thống mật mã mạnh hơn, theo sau đó, hệ thống mật mã đường cong elip khó bị phá vỡ hơn RSA và Diffie-Hellman.

Mật mã ECC cung cấp tính an toàn tương đương với các hệ mật khóa công khai truyền thống, trong khi độ dài khóa nhỏ hơn nhiều lần. Người ta đã ước lượng rằng cỡ khoá 3248 bit của hệ mật RSA cho cùng một độ an toàn như 256 bit của hệ mật ECC. Điều đó có nghĩa là việc cài đặt ECC sử dụng tài nguyên hệ thống ít hơn, năng lượng tiêu thụ nhỏ hơn.... Với ưu thế về độ dài khóa nhỏ, ECC đang được ứng dụng rộng rãi trong nhiều lĩnh vực.



Để hình dung mức độ khó phá vỡ hơn bao nhiêu, Lenstra mới đây đã giới thiệu khái niệm "An ninh toàn cầu". Bạn có thể tính toán lượng năng lượng cần thiết để phá vỡ thuật toán mật mã và so sánh với lượng nước mà năng lượng có thể đun sôi. Theo biện pháp này, việc phá khóa RSA 228 bit đòi hỏi ít năng lượng hơn so với việc đun sôi một muỗng cà phê nước. Một cách tương đối, việc phá khóa đường cong elip 228 bit đòi hỏi đủ năng lượng để đun sôi tất cả nước trên trái đất. Đối với mức bảo mật này với RSA, bạn cần một khóa có 2.380 bit.

### 2. Định nghĩa

Trong toán học, đường cong elip là một đường cong đại số trơn, trên đó có một điểm $\theta$ xác định. Một đường cong elip được xác định trên một trường K và mô tả các điểm trong không gian $K ^ 2$, tích Descartes của K với chính nó. Elliptic curves có thể được định nghĩa trong mọi trường K; Nếu đặc tính của trường khác với 2 và 3 thì đường cong có thể được mô tả như một đường cong đại số phẳng chứa các nghiệm (x, y) cho:

$$y^{2}=x^{3}-px-q$$

Đối với một số hệ số p và q thuộc K. Đường cong bắt buộc phải không suy biến, nghĩa là đường cong không có đỉnh hoặc tự giao nhau. Với điểm O là điểm duy nhất ở vô cực. Ở đây hệ số p và q trong đa thức $x ^ 3 − p * x − q$ phải không có bất kỳ nghiệm kép nào. Từ đó ta có điều kiện $\Delta = 4 * p ^ 3 - 27 * b ^ 2 \neq 0$.(Điều này tương đương với điều kiện là không vuông góc trong x.)

Ngoài ra, trong cấu trúc đại số nó được xếp trong nhóm aben với phép ánh xạ là phép cộng và điểm đơn vị là điếm $\theta$. 

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/80efdcd6-bbca-4e47-9429-2380f851ee24)

VD: $y ^ 2 = x ^ 3 + 2 * x + 3$

Ngoài ra, nó còn có dạng đặc biệt : $y ^ {2} + a_{1} * x * y + a_{3} * y = x ^ {3} + a_{2} * x ^ {2} + a_{4} * x + a_{6}$ đây còn được gọi là phương trình Weierstrass(tổng quát hơn phương trình ở trên).

Với một điểm L trên K thuộc không gian $K ^ 2$ là (x, y) được định nghĩa là điểm thỏa mãn phương trình elliptic. Khi điểm L ở vô cực được coi là đơn vị $(a_{6}, 0)$

![imageimage](https://images.viblo.asia/full/41f7339d-299e-4304-89a8-7c08c101e282.gif)

Đây là hình ảnh của "đường cong" này trong không gian 3 chiều.

Nhìn kỹ hơn vào đường cong elip được vẽ ở trên. Nhận thấy, một trong số đó là đối xứng ngang. Bất kỳ điểm nào trên đường cong đều được phản ánh qua trục x và vẫn giữ nguyên đường cong. Một đặc tính thú vị hơn là bất kỳ đường thẳng nào cũng sẽ cắt đường cong ở nhiều nhất là ba điểm.

Chúng ta hãy tưởng tượng đường cong này là bối cảnh cho một trò chơi bi-a kỳ quái. Lấy hai điểm bất kỳ trên đường cong và vẽ một đường thẳng qua chúng, nó sẽ cắt đường cong tại đúng một điểm nữa. Trong trò chơi bi-a này, bạn lấy một quả bóng tại điểm A, bắn nó về phía điểm B. Khi nó chạm đường cong, quả bóng nảy thẳng lên (nếu nó nằm dưới trục x) hoặc thẳng xuống (nếu nó ở trên trục x) sang phía bên kia của đường cong.

Việc này chỉ ra rằng nếu có hai điểm, với điều kiện một điểm thực hiện “(+)” chính nó n lần ra điểm còn lại, thì việc tìm ra n khi mà chỉ biết điểm đầu và điểm cuối là rất khó khăn. Áp dụng cho chính ví dụ về trò billiard, nếu một người chơi trò chơi này một mình trong một căn phòng trong một khoảng thời gian ngẫu nhiên. Rất dễ dàng cho anh ta để đánh bi đi theo các quy tắc mô tả ở trên. Đến khi một người khác bước vào phòng sau đó và nhìn thấy vị trí viên bi, ngay cả khi họ biết tất cả các quy tắc của trò chơi và vị trí bắt đầu, họ không thể xác định số lần viên bi được đánh mà không chơi qua toàn bộ trò chơi một lần nữa. Dễ thực hiện, khó suy ngược, đây chính là tính chất của một phương pháp mã hóa tốt.

#### 2.1. Luật nhóm

![image](http://blog.cloudflare.com/content/images/image02.gif)

Luật nhóm là một khái niệm cơ bản trong mật mã đường cong elip (ECC) xác định cách các điểm trên đường cong elip có thể được kết hợp để tạo ra các điểm mới trên đường cong. Luật nhóm cho các đường cong elip tạo thành cơ sở cho các phép toán như cộng điểm và nhân vô hướng, những phép toán này rất quan trọng để thực hiện các thuật toán mã hóa.

Định luật nhóm trên đường cong elip được định nghĩa như sau:

+ Cộng điểm (P + Q):

Cho hai điểm phân biệt $P$ và $Q$ trên đường cong elip, định luật nhóm xác định phép cộng các điểm này để tạo ra điểm thứ ba $R$, ký hiệu là

$$P + Q = R$$

Về mặt hình học, nếu đường thẳng đi qua P và Q cắt đường cong tại điểm thứ ba, kết quả là sự phản chiếu của điểm này qua trục x R. Nếu như P và Q cùng điểm, định luật nhóm xác định tiếp tuyến tại điểm đó và tìm giao điểm thứ ba.

+ Phần tử nhận dạng ($\theta$ hoặc $\infty$):

Có một điểm đặc biệt trên đường cong elip gọi là phần tử đồng nhất, thường được ký hiệu là $\theta$ hoặc $\infty$ (vô cùng). Điểm này đóng vai trò là đồng nhất thức cộng trong luật nhóm. Đối với bất kỳ điểm P nào trên đường cong,

$$P + \theta = \theta + P = P$$

$$P + \infty = \infty + P = P$$

+ Phần tử nghịch đảo (Phủ định):

Đối với bất kỳ điểm $P$ nào trên đường cong elip tồn tại một điểm $-P$ sao cho

$$P + (−P) = \theta$$

trong đó $−P$ là sự phản ánh của P qua trục x.

+ Tính kết hợp:

Luật nhóm trên đường cong elip có tính kết hợp. Cho ba điểm $P, Q, R$ trên đường cong,

$$(P+Q)+R=P+(Q+R)$$
  
Luật nhóm cho phép xây dựng một nhóm toán học bằng cách sử dụng tập hợp các điểm trên đường cong elip. Nhóm này được sử dụng trong ECC cho các hoạt động mã hóa khóa công khai, chẳng hạn như trao đổi khóa, chữ ký số và mã hóa khóa chung. Độ khó của bài toán logarit rời rạc trên đường cong elip tạo cơ sở cho tính bảo mật của các hoạt động mật mã này.

Hiểu luật nhóm là rất quan trọng để thực hiện các thuật toán mật mã đường cong elip và đảm bảo tính an toàn và hiệu quả của các hệ thống mật mã dựa trên các đường cong elip.

#### 2.2 Phương trình dạng đơn giản

Như đã nói ở trên ta có thể thấy phương trình ecc có nhiều dạng khác nhau nhưng trong crypto thường chỉ sử dụng dạng đơn giản.

Thông qua các phép biến đổi cở bản (cơ bản nhưng em đọc cx không hiểu gì :v) như:

+ Biến đổi từ Dạng Edwards về Weierstrass ($a *x ^ 2 + y ^  2 = 1 + d * {x ^ 2} * {y ^ 2}$)
+ Biến đổi từ Dạng Montgomery về Weierstrass ($B * y ^ 2 = x ^ 3 + A * {x ^ 2} + x$)
+ Biến đổi từ Dạng Jacobi về Weierstrass ($y ^ 2 = x ^ 3 + A * {x ^ 2} + x$)

Phương trình của đường cong elip (elliptic curve) trong dạng đơn giản, thường là phương trình Weierstrass, có ý nghĩa quan trọng trong elliptic curve cryptography (ECC) và các hệ thống mã hóa dựa trên đường cong elip. Dạng đơn giản giúp tối ưu hóa các phép toán và triển khai của hệ thống mã hóa. Dưới đây là một số ý nghĩa chính:

 + Thuận Tiện Cho Phép Toán:

Dạng đơn giản của phương trình Weierstrass tạo ra cấu trúc nhóm trên đường cong elip mà không làm giảm đi tính toán. Các phép toán như cộng điểm và nhân số nguyên trở nên hiệu quả và đơn giản hóa.
 + Tính Đồng Nhất:

Việc sử dụng một dạng phương trình chung (ví dụ: phương trình Weierstrass) giúp tạo ra một chuẩn hóa trong triển khai của ECC. Các hệ thống có thể sử dụng cùng một dạng phương trình chung, giúp tích hợp và tương tác giữa các hệ thống dễ dàng hơn.
Chia Sẻ Điểm:

Dạng đơn giản thường làm cho việc chia sẻ các điểm trên đường cong elip trở nên dễ dàng. Các tiêu chuẩn được xây dựng dựa trên các dạng phương trình thông thường như phương trình Weierstrass, giúp đảm bảo tính tương thích và tích hợp trong các ứng dụng và giao thức khác nhau.
 + Bảo Mật:

Một số dạng phương trình đơn giản được chọn để đảm bảo tính an toàn và khả năng chống lại các tấn công. Các tham số trong phương trình phải được chọn cẩn thận để tránh các loại tấn công như tấn công động (side-channel attacks) và các vấn đề khác liên quan đến an ninh hệ thống mã hóa.
+ Hiệu Năng:

Dạng đơn giản giúp cải thiện hiệu suất của hệ thống mã hóa. Đối với các thiết bị có tài nguyên hạn chế như thiết bị di động hoặc IoT, việc sử dụng dạng phương trình đơn giản có thể là quyết định quan trọng để đạt được hiệu suất tốt.
Thuận Lợi Cho Triển Khai Trên Phần Cứng:

Các thiết bị có tài nguyên hạn chế thường thích hợp với đường cong elip có dạng đơn giản. Các phép toán như cộng điểm và nhân số nguyên trên đường cong Weierstrass thường có thể được triển khai một cách hiệu quả trên phần cứng nhúng.
Dạng đơn giản của phương trình đường cong elip không chỉ giúp tối ưu hóa tính toán mà còn làm cho các hệ thống mã hóa dựa trên ECC trở nên linh hoạt, hiệu quả và dễ quản lý.

#### 2. 3 ECC order

> định lý Hasse

Với N là số phần tử trên elliptic curve trong trường p, ta có 
    
$$|N - (p + 1)| \leq 2 * \sqrt{p}$$


Việc tính toán "order" của một đường cong elliptic trên trường hữu hạn Fp có thể trở nên rất phức tạp, và cần sử dụng các thuật toán đặc biệt để giải quyết vấn đề này. Một trong những phương pháp tính toán "order" của một đường cong elliptic là thuật toán Schoof.

Tuy nhiên, nếu đường cong elliptic được xác định trên trường Fp và có thể được viết dưới dạng y^2 = x^3 + ax + b (mod p) (với a, b là các số nguyên trong trường Fp), thì theo định lý Hasse, ta có thể xác định được giới hạn trên và dưới cho "order" của đường cong elliptic đó như sau:

Vậy với order của E(p) là số phần tử trên đường cong ký hiệu |E(k)|, vậy $|E(p)| = p + 1 - 2 * \sqrt{p}$

Cụ thể hơn, ta có thể tính toán Group order của E(K) bằng cách tìm số lượng điểm trên đường cong, sử dụng các thuật toán tìm điểm trên đường cong như phép cộng và phép nhân. Việc tính toán Group order rất quan trọng trong việc áp dụng đường cong elliptic trong các ứng dụng mật mã, như tạo số nguyên tố trong mã hóa RSA.

#### 2. 4 ECC subgroup order

Trong elliptic cuvre, nhóm con được định nghĩa là bậc của một phần tử thuộc đường cong mà sau khi nhân điểm đó với một số ta sẽ được một điểm vãn thuộc đường cong. Như vậy, với điểm P sao cho thỏa mãn $P * n = Q, n \in N$ khiến Q thuộc đường cong. Bậc của P là số lượng phần tử thỏa mãn tính chất trên(số lượng điểm trên nhóm con). 

Theo định lý la-gờ-răng (?) thì cấp của nhóm con là ước chung của cấp đường cong.

Vậy với đường cong trên trường $F_p$, p là số nguyên tố, thì cấp của một phần tử có thể là 1 hoặc p. Điều này là cơ sở cho việc sử dụng đường cong elliptic trong ECC, vì nếu một điểm P trên đường cong có bậc nhóm con bằng p thì P có thể được sử dụng như một Base Point để tạo ra các khóa bảo mật trong hệ thống ECC.

#### 2. 5 Base point

Điểm cơ sở (base point) là điểm thuộc đường cong thỏa mãn:

+ Điểm cơ sở phải thuộc đường cong
+ Cấp của điểm cơ sở phải đủ lớn(tức số lượng điểm có thể tạo ra từ điểm cơ sở lớn để đảm bảo tính bảo mật)
+ Không có số nguyên dương nào khác 0 nhân với điểm đó tạo ra điểm vô cùng.

Hiện nay có một vài cách để tìm ra điểm cơ sở, dễ dàng nhất pà cách thử và sai tức là ta cứ thử cho tới khi nào tìm được điểm thỏa mã thì dừng lại. Một cách khác đó là Pollard rho hay kangaroo nhưng phương pháp này thường chỉ được áp dụng cho các đường cong "nhỏ".

Việc tìm một base point tốt ká quan trong trong crypto vì nó sẽ ảnh hưởng tới tính bảo mật, thời gian, hiệu suất của hệ thống.

#### 2. 6 Phép cộng

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/9ab9490b-3267-4e9b-add6-0c26d1ba54a6)

$$E: y ^ 2 = x ^ 3 + a * x + b$$

Phép cộng hai điểm trên đường cong elliptic được thực hiện bằng cách sử dụng công thức cộng.

Với hai điểm P, Q thuộc đường cong ta tính P + Q như sau:

+ Nếu P = $\theta$, thì Q + P = Q
+ Nếu Q = $\theta$, thì Q + P = P
+ Nếu P = - Q (cũng tương tự Q = - P) hay hai phần tử đối xứng nhau qua trục hoành (phần tử nghịch đảo), thì P + Q = $\theta$
+ Còn lại ta thực hiện như sau:
  + Tính độ dốc của đoạn thẳng được tạo ra bởi P, Q. Nếu P, Q trùng nhau thì đoạn thẳng là tiếp tuyến của đường cong tại điểm P, Q
  + Tìm giao điểm của đường này với đường cong
  + Lấy điểm đối xứng của điếm có, điểm đó là điểm cần tìm
 
Công thức chi tiết để tính toán điểm phản xạ R qua trục hoành là:

+ $s = (y_P - y_Q) / (x_P - x_Q)$

+ $x_R = s^2 - x_P - x_Q$

+ $y_R = -y_P + s * (x_P - x_R)$


TÍnh toán phép công là cơ sở để xây dựng nên hệ mật ECC, và nhiều vấn đề toán học khác.

#### 2. 7 Phép nhân

Phép nhân định nghĩa như một dãy các phép công liên tiếp với nhau $n * P = P + P ... + P = (n - 1) * P + P$

Việc tính toán phép nhân vô hướng này có thể được tối ưu bằng cách sử dụng các thuật toán như Montgomery ladder hay double-and-add. Các thuật toán này giúp giảm số lần tính toán trên đường cong Elliptic và tăng tốc độ tính toán.

Ta thực hiện như sau:
+ Set Q = P and R = O.
+ Loop while n > 0.
  + If n ≡ 1 mod 2, set R = R + Q.
  + Set Q = 2 Q and n = ⌊n/2⌋.
  + If n > 0, continue with loop at Step 2.
+ Return the point R, which equals nP.

#### 2. 8 Discrete log

Trong nhóm nhân Zp*, cho các phần tử r và q của nhóm và một số nguyên tố p, tìm một số k sao cho r = qk mod p. Khi nhóm đường cong elip được mô tả bằng ký hiệu cộng, bài toán logarit rời rạc đường cong elip là: cho điểm P và Q trong nhóm, tìm một số k sao cho Pk = Q, k được gọi là log rời rạc cơ số P của Q. 

Bất kỳ một hệ mật khóa công khai nào cũng phải sử dụng một bài toán khó để xây dựng hàm một chiều. Ý nghĩa một chiều ở đây có nghĩa là tính thuận thì dễ (thuật toán giải trong thời gian đa thức) và tính ngược thì khó (thuật toán giải với
thời gian không phải là đa thức - thường là hàm mũ hoặc nửa mũ). Các tham số của Hệ mật dựa trên đường cong Elliptic (ECC) cần phải được lựa chọn cẩn thận để tránh được các tấn công đối với bài toán ECDLP.
Trong trường hợp p nhỏ, ta có thể tình k bằng cách thử tất cả các số nguyên có thể trong khoảng từ [1: p - 1] để tìm ra số nguyên k. Nhưng đây là một cách làm khá lâu, với các bài toán lớn nó dường như trở nên bất khả thi với độ phức tập O(n).Trong trường hợp xấu nhất sẽ phải cần đến n bước
thử, trung bình thường là n/2 là đạt được điểm Q, do đó cần phải chọn n đủ lớn để bài toán vét cạn là không khả thi (n ≥ 2160).

Thuật toán tốt nhất hiện nay để tấn công bài toán ECDLP là sự kết hợp của thuật toán Pohlih-Hellman và Pollard’s rho, thuật toán này có thời gian tính là O($sqrt{p}$
), với p là ước số nguyên tố lớn nhất của n do đó phải chọn số n sao cho nó chia hết số nguyên tố p lớn nhất có 
 đủ lớn để giải bài toán này là không khả
thi.


### 3. Phương pháp tính discrete log

#### 3.1 Phương pháp bước nhỏ bước lớn

```py

from gmpy2 import iroot


def baby_gaint(a, b, p) -> int:
    m = iroot(p, 2)[0] + 1

    tmp = {}

    for i in range(0, m):
        tmp[pow(a, i, p)] = i

    y = b
    for i in range(0, m):
        try:
            j = tmp[y]
            return ( i * m + j)
        except:
            y = y * pow(a, -m, p)

    return None

```

Đây là code babystep giantstep mình viết để giải $a ^ x = b \pmod{p}$ thông thường.

Thuật toán này dựa trên sự đánh đổi không-thời gian. Đó là một sửa đổi khá đơn giản của phép nhân thử, phương pháp ngây thơ để tìm logarit rời rạc. Với một nhóm hoán vị E(p), phần tử sinh a và một phần tử trong nhóm b. Ta tìm số x sao cho $a = x * b \pmod{p}$. Độ phức tạp của nó là O($sqrt{n}$) thay vì O(n) như brute-force.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/94a2bc1b-d77f-48eb-8c14-10f3fbc8ec3c)

Tương tự như thế, giả sử tồn tại x = i * m + j với m = $\sqrt{p}$ nên $a = (i * m + j) * b \pmod{p}$ $\to$ $a - i * m * b = j * b \pmod{p}$

từ đó thử với mọi i, j trong khoảng $1 \leq j, i \leq p - 1$ thử lưu cặp (j, j * b) và tính (a - i * m * b) nếu thỏa mãn thì ta tìm ra được $x = m * i + j$
