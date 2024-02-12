
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

![image](https://images.viblo.asia/full/41f7339d-299e-4304-89a8-7c08c101e282.gif)

Đây là hình ảnh của "đường cong" này trong không gian 3 chiều.

Nhìn kỹ hơn vào đường cong elip được vẽ ở trên. Nhận thấy, một trong số đó là đối xứng ngang. Bất kỳ điểm nào trên đường cong đều được phản ánh qua trục x và vẫn giữ nguyên đường cong. Một đặc tính thú vị hơn là bất kỳ đường thẳng nào cũng sẽ cắt đường cong ở nhiều nhất là ba điểm.

Chúng ta hãy tưởng tượng đường cong này là bối cảnh cho một trò chơi bi-a kỳ quái. Lấy hai điểm bất kỳ trên đường cong và vẽ một đường thẳng qua chúng, nó sẽ cắt đường cong tại đúng một điểm nữa. Trong trò chơi bi-a này, bạn lấy một quả bóng tại điểm A, bắn nó về phía điểm B. Khi nó chạm đường cong, quả bóng nảy thẳng lên (nếu nó nằm dưới trục x) hoặc thẳng xuống (nếu nó ở trên trục x) sang phía bên kia của đường cong.

Việc này chỉ ra rằng nếu có hai điểm, với điều kiện một điểm thực hiện “(+)” chính nó n lần ra điểm còn lại, thì việc tìm ra n khi mà chỉ biết điểm đầu và điểm cuối là rất khó khăn. Áp dụng cho chính ví dụ về trò billiard, nếu một người chơi trò chơi này một mình trong một căn phòng trong một khoảng thời gian ngẫu nhiên. Rất dễ dàng cho anh ta để đánh bi đi theo các quy tắc mô tả ở trên. Đến khi một người khác bước vào phòng sau đó và nhìn thấy vị trí viên bi, ngay cả khi họ biết tất cả các quy tắc của trò chơi và vị trí bắt đầu, họ không thể xác định số lần viên bi được đánh mà không chơi qua toàn bộ trò chơi một lần nữa. Dễ thực hiện, khó suy ngược, đây chính là tính chất của một phương pháp mã hóa tốt.

#### 2.1. Luât nhóm

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
