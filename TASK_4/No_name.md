
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

Dễ thấy khi n lớn ( với n nhỏ thì không sao) thì việc tính từng P công với nhau là rất tốn thời gian và hiệu năng(cái tư bản không thích) nên ta sử dụng thuật toán double and add để tính toán.

với $n * P = n_0 * Q_0 + n_1 * Q_1 + n_2 * Q_2 + ··· + n_r * Q_r$.

$Q_0 = P, Q_1 = 2 * Q_0, Q_2 = 2 * Q_1, ... ,Q_r = 2 * Q_{r−1}$.

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

Việc khó đầu tiên là với hai điểm P, Q bất kỳ không phải lúc nào việc tính log rời rạc của nó cũng tồn tại và xác định, tuy nhiên trong bài toán mã hóa người ta luôn chọn P sao cho xác định được Q từ đó log của nó hoàn toàn xác định và bằng n.

Việc khó thứ hai là với hai điểm P, Q ta có thể tìm ra được nhiều điểm n thỏa mãn từ đó ta phải hướng tới việc tìm n nhỏ nhất. Dễ chứng minh nó như sau, giả sử n * P = $\theta$, từ đó 2 * n * P = $\theta$, 3 * n * P = $\theta$, ... 

từ đó ta có một tính chất khá hay (nhưng không biết áp dụng dc k )

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/7871a18d-f357-45b4-bf13-4f22c3c97d18)


#### 2. 9 ECC over finite fields

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/367f66ec-b3df-4e0a-8789-46e17645cb7e)

Với định nghĩa như vậy ta lại nảy sinh một vấn đề rằng với mỗi x thuộc ${E(F_p) : Y ^ 2 = X ^ 3 + a * X + b}$ ta luôn có $y ^ 2 \equiv c \pmod{p}$ từ đó ta phải tìm thặng dư bậc hai với mội x để tìm được ra hai nghiệm y thỏa mãn.

VD:
$E : Y ^ 2 = X ^ 3 + 3 * X + 8$ over the field F13.

$5 ^ 2 ≡ 12 (mod 13)$  và  $8 ^ 2 ≡ 12 (mod 13)$.
tương tự như vậy ta có được tất cả các phần tử của đường cong trong trường hữu hạn.

E(F13) = {O,(1, 5),(1, 8),(2, 3),(2, 10),(9, 6),(9, 7),(12, 2),(12, 11)}.

Từ đó ta có bảng sau:

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/84ceaba6-4943-433a-b100-43524938bd81)



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

### 4. ECC in crpytography

#### 4. 1 Diffie hellman key exchange

Nó khá giống với trao đổi khóa trong RSA, nên mình sẽ nói(cụ thể là viết) nhanh.

Alice và Bob tạo ra một đường cong chung sử dụng dạng như đã nói ở trên và một điểm P thuộc đường cong.

Alice trong ra một số bí mật là a và giữ nó làm bí mất k để cho ai biết kể cả Bob. Tương tự Bob cũng tạo ra một số b.

Alice và Bob tính:

$$Q_A = a * P \text{và} Q_B = b * P $$

Sau đó thì Alice gửi cho Bob $Q_A$ Bob gửi cho Alice $Q_B$. Từ đó ta có thể tính ra số bí mật chung là:
$$secret = a * Q_B = b * Q_A = a * b * P$$

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/e498c030-cfc5-4a12-bf7d-f44abc7cff6c)

(Ảnh minh họa)

#### 4. 2 EEPKC

Mã hóa nãy cũng gần giống như RSA => :(

Alice và Bob tạo ra một đường cong chung sử dụng dạng như đã nói ở trên và một điểm P thuộc đường cong. Với thông điệp muốn gửi là M.

Alice chọn ra một số bí mật là a(giữ số này k cho ai biết).

Alice tính : $Q_a = a * P$

Rồi sau đó chon một số k ngẫu nhiên có thể để lộ, rồi tính: $c_1 = k * P$ và $c_2 = M + k * Q_a$

Rồi gửi hai điểm trên là được.

Ta sẽ giả mã nó bằng cách như sau: $M = c_2 - a * c_1 = M + k * a * P - a * k * P = M$ :v đơn giảm mà.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/3523f254-ff04-489f-8548-7e4ec87146c2)

(Hình minh họa)

#### 4. 3 ECDSA

Giả sử Alice và Bob muốn trao đổi với nhau thì họ phải thảo thuận một đường cong chung gồm (curve, n, G), trong đó curve là các tham số của đường cong, n là cấp của G, G là điểm cơ sở.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/607810c1-6c25-4a89-9e83-65a18f37753c)

Dể ký một tin nhắn ta làm theo các bước sau:

Chọn một số bí mật $d_a$, trong khoảng [1, n - 1]

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/4fa1316d-6e7b-498d-90fb-2d23902ff5b0)

rồi gửi các tham số vừa tính đựo cho Bob, khi đó, để xác nhận tin nhắn đã được gửi là đúng Bob xác nhận lại như sau:

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/096cf05b-dbfa-4410-b2ed-122d0a0b382e)

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/bab8c7ce-b2b1-46c3-a023-7eeea31945b0)

(Hình minh họa)

*More*

Mỗi khi ký một tin nhắn ta cần chọn các k khác nhau để tranh bị tấn công theo cách sau:

giả sử ta bắt được hai mã xác thực (r, s) và (r', s'). Do được mã hóa cũng bằng k nên khi đó r = r'.  mà  

$s = k ^ {-1} * ( z + r *d_{A}) \pmod{n}$

khi đó s - s' = k* (z - z'), từ đó k = (s - s')/ (z - z') nên ta có thể tìm k (vì z , z' đã biết) từ đó hoàn toàn có thể tính lại $d_A = (s * k - z) / r$

## I. Write up

### 1. Background Reading

---

**_TASK:_**

Formally, let E be an elliptic curve, point addition has the following properties

(a) P + O = O + P = P
(b) P + (−P) = O
(c) (P + Q) + R = P + (Q + R)
(d) P + Q = Q + P

In ECC, we study elliptic curves over a finite field Fp. This means we look at the curve modulo the characteristic p and an elliptic curve will no longer be a curve, but a collection of points whose x,y coordinates are integers in Fp.

The following starter challenges will take you through the calculations for ECC and get you used to the basic operations that ECC is built upon, have fun!

Property (d) shows that point addition is commutative. The flag is the name we give groups with a commutative operation.

---

Tính chất d) là tính chất giao hoán, theo kiến thức đã học từ TASK3 ta dễ thấy đó là nhóm aben còn gọi là nhóm giao hoán.

> crypto{abelian}


 ### 2. Point Negation

---

**_TASK:_**

 E: Y2 = X3 + 497 X + 1768, p: 9739

Using the above curve, and the point P(8045,6936), find the point Q(x,y) such that P + Q = O.

---

Ta có điểm để thảo mãn P + Q = 0 là điểm đối xứng với nó qua trục hoành, nên ta chỉ cần lấy nghịch đảo hệ số P_y là được (lưu ý do đây đang là trong nhóm hữu hạn nên ta lấy thành p - P_y)


> crypto{8045, 2803}


### 3. Point Addition


---

**_TASK:_**

We will work with the following elliptic curve, and prime:

$$E: Y^2 = X^3 + 497 * X + 1768,\quad p: 9739$$

You can test your algorithm by asserting: $X + Y = (1024, 4440)$ and $X + X = (7284, 2107)$ for $X = (5274, 2841)$ and $Y = (8669, 740)$.


Using the above curve, and the points $P = (493, 5564), Q = (1539, 4742), R = (4403,5202)$, find the point $S(x,y) = P + P + Q + R$ by implementing the above algorithm.

---

Dựa theo kiến thức đã học ở bên trên, dùng thuật toán cộng điểm để tính điểm S = 2P + Q + R;
Sau khi tính được tạo độ điểm S có thể thay tọa độ S vào E để kiểm tra.
Ta dùng thuật toán cộng điểm đã trình bày ở trên tiến hành cộng từng điểm 1, rồi lấy kết quả cộng với điểm tiếp theo. Cụ thể tính 2P trước sau đó tính 2P + Q và cuối cùng 2P + Q + R.

P + P + Q + R = (P + P) + (Q + R)

```python


def add_point(p, q, a, b, n):
    if p[1] == 0:
        return q
    elif q[1] == 0:
        return p
    elif p[0] == q[0] and p[1] == -q[1]:
        return (0, 0)
    else:
        if p[0] == q[0] and p[1] == q[1]:
            m = ((3 * (p[0] ** 2) + a) * pow(2 * p[1], -1, n) ) % n
        else:
            m = ((q[1] - p[1]) * (pow(q[0] - p[0], -1, n))) % n

        x = (m ** 2 - q[0] - p[0]) % n
        y = (m * (p[0] - x) - p[1]) % n
        return (x, y)
    
a = 497
b = 1768
n = 9739

P = (493, 5564)
Q = (1539, 4742)
R = (4403,5202)

print(add_point(add_point(P, P, a, b, n), add_point(Q, R, a, b, n), a, b, n))


```

> crypto{4215, 2162}

### 4. Scalar Multiplication

---

**_TASK:_**

We will work with the following elliptic curve, and prime:

$$E: Y2 = X3 + 497 X + 1768,\quad p: 9739$$

You can test your algorithm by asserting: $1337 * X = (1089, 6931)$ for $X = (5323, 5438)$.


Using the above curve, and the points $P = (2339, 2213)$, find the point $Q(x,y) = 7863 * P$ by implementing the above algorithm.

After calculating $Q$, substitute the coordinates into the curve. Assert that the point $Q$ is in $E(Fp)$.


---

Bài này chỉ đơn giản là thực hiện nhiều lần phép cộng điểm, do số khá lớn nên ta áp dụng cách cộng điểm double and add đã được nhắc đến ở trên(nếu k tin có thể lên xem lại)

```python



def add_point(p, q, a, b, n):
    if p[1] == 0:
        return q
    elif q[1] == 0:
        return p
    elif p[0] == q[0] and p[1] == -q[1]:
        return (0, 0)
    else:
        if p[0] == q[0] and p[1] == q[1]:
            m = ((3 * (p[0] ** 2) + a) * pow(2 * p[1], -1, n) ) % n
        else:
            m = ((q[1] - p[1]) * (pow(q[0] - p[0], -1, n))) % n

        x = (m ** 2 - q[0] - p[0]) % n
        y = (m * (p[0] - x) - p[1]) % n
        return (x, y)

def multiplitcation(p, a, b, m, n):
    q = p
    r = (0, 0)

    while n > 0:
        if n % 2 == 1:
            r = add_point(r, q, a, b, m)
        q = add_point(q, q, a, b, m)
        n //= 2
    return r

a = 497
b = 1768
m = 9739

P = (2339, 2213)
n = 7863

print(multiplitcation(P, a, b, m, n))


```

> crypto{9467, 2742}


### 5. Curves and Logs

---

**_TASK:_**

$$E: Y2 = X3 + 497 X + 1768,\quad p: 9739,\quad G: (1804,5368)$$

Calculate the shared secret after Alice sends you $Q_A = (815, 3190)$, with your secret integer $n_B = 1829$.

Generate a key by calculating the SHA1 hash of the x coordinate (take the integer representation of the coordinate and cast it to a string). The flag is the hexdigest you find.****

---


Bài này có nói đểm cách chuyển khóa diffie-hellman, và ta đã có sãn tọa độ điểm của alice rồi nên bây giờ ta chỉ cần tính Q_a * n_b theo code đã viết sãn ở trên (giống y sì bài trước là ta có đáp án)


```python


from hashlib import sha1
from Crypto.Util.number import bytes_to_long, long_to_bytes

def add_point(p, q, a, b, n):
    if p[1] == 0:
        return q
    elif q[1] == 0:
        return p
    elif p[0] == q[0] and p[1] == -q[1]:
        return (0, 0)
    else:
        if p[0] == q[0] and p[1] == q[1]:
            m = ((3 * (p[0] ** 2) + a) * pow(2 * p[1], -1, n) ) % n
        else:
            m = ((q[1] - p[1]) * (pow(q[0] - p[0], -1, n))) % n

        x = (m ** 2 - q[0] - p[0]) % n
        y = (m * (p[0] - x) - p[1]) % n
        return (x, y)

def multiplitcation(p, a, b, m, n):
    q = p
    r = (0, 0)

    while n > 0:
        if n % 2 == 1:
            r = add_point(r, q, a, b, m)
        q = add_point(q, q, a, b, m)
        n //= 2
    return r

a = 497
b = 1768
m = 9739
G = (1804,5368)

q = (815, 3190)
nB = 1829



hash = sha1()
hash.update(str(multiplitcation(q, a, b, m, nB)[0]).encode())
print(hash.hexdigest())



```

### 6. Efficient Exchange


---

**_TASK:_**

E: Y2 = X3 + 497 X + 1768, p: 9739, G: (1804,5368)

Calculate the shared secret after Alice sends you q_x = 4726, with your secret integer nB = 6534.

Use the decrypt.py file to decode the flag

{'iv': 'cd9da9f1c60925922377ea952afc212c', 'encrypted_flag': 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'}

---

