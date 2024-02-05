
Tables of contens
=================
*[I. Tổng quát](#i-Tổng-quát)

*[II. Write up](#ii-Writes-up)


## I. Tổng quát

### 1. Group (Nhóm)

Trong toán học, một nhóm (group) là một tập hợp các phần tử được trang bị một phép toán hai ngôi kết hợp hai phần tử bất kỳ của tập hợp thành một phần tử thứ ba thỏa mãn bốn điều kiện gọi là tiên đề nhóm, lần lượt là tính đóng, tính kết hợp, sự tồn tại của phần tử đơn vị và tính khả nghịch. Một trong những ví dụ quen thuộc nhất về nhóm đó là tập hợp các số nguyên cùng với phép cộng; khi thực hiện cộng hai số nguyên bất kỳ luôn thu được một số nguyên khác. Hình thức trình bày trừu tượng dựa trên tiên đề nhóm, tách biệt nó khỏi bản chất cụ thể của bất kỳ nhóm đặc biệt nào và phép toán trên nhóm, cho phép nhóm bao trùm lên nhiều thực thể với nguồn gốc toán học rất khác nhau trong đại số trừu tượng và rộng hơn, và có thể giải quyết một cách linh hoạt, trong khi vẫn giữ lại khía cạnh cấu trúc căn bản của những thực thể ấy. Sự có mặt khắp nơi của nhóm trong nhiều lĩnh vực bên trong và ngoài toán học khiến chúng trở thành nguyên lý tổ chức trung tâm của toán học đương đại.

Ví dụ: Một trong những nhóm cơ bản nhất là nhóm số nguyên cùng với phép cộng. Hoặc các nhóm khác cũng tương tự như nhóm số thực, nhóm số phức, nhóm đa thức bậc n với hệ số thực, v.v...

### 2. Tính chất

#### a. Luật hợp thành trong

Luật hợp thành trong trên tập E, hay phép toán trên E, là quy luật khi tác động lên hai phần tử a và b của E sẽ tạo ra một và chỉ một phần tử cũng thuộc E.
Nói cách khác: Luật hợp thành trong trên tập E là một ánh xạ từ $E * E \to E$

Ký hiệu: $*$

$$(a, b) \in E \quad \mapsto \quad a * b \in E$$

Ví dụ: Cũng với nhóm số nguyên ở trên với phép cộng ta dễ thấy $R * R \mapsto R$ nên đây là một hợp thành trong.

#### b. Cấu trúc Nhóm

Cho một tập hợp $G \neq \emptyset$ và một phép toán $(*)$. Ký hiệu $(G, *)$

Cặp $(G, *)$ được gọi là một nhóm nếu thỏa mãn các tính chất sau:

+ Tính kết hợp $\forall a, b, c \in G$ ta có: $abc = a(bc) = (ab)c$
+ Có phần tử trung hòa $\forall x \in G$, $\exists e \in G$ sao cho: $x * e = x$
+ Có phần tử đối $\forall x \in G$, $\exists x' \in G$  sao cho: $x * x' = e$ với e là phần tử trung hòa

Ngoài ra, nếu nhóm có tính giao hoán ta gọi là nhóm Abel, thỏa mãn: $(ab)c = a(bc)$ $\forall a, b, c \in G$ 

Ví dụ: Với nhóm (R, +), ta dễ thấy:

+ Tính kết hợp $\forall a, b, c \in R$ ta có: $a + b + c = a + (b + c) = (a + b) + c$
+ Có phần tử trung hòa $\forall x \in r$, $\exists 0 \in R$ sao cho: $x + 0 = x$
+ Có phần tử đối $\forall x \in R$, $\exists -x \in R$  sao cho: $x + (-x) = 0$ với 0 là phần tử trung hòa
+ Có tính giao hoán: $(a + b) + c = a + (b + c)$ $\forall a, b, c \in R$

Vậy (R, +) là một nhóm Abel.

#### c. Một số tính chất

1. Phần tử trung hòa $e$ là duy nhất.
2. Phần tử đối $x'$ của $x$ là duy nhất.
3. Có quy tắc giản ước: $a ∗ x = a ∗ y \to x = y$
4. Phương trình $x ∗ a = b$ có nghiệm duy nhất $x = b ∗ a'$

Thật vậy, theo ví dụ trên (R, +) ta hoàn toàn khồn thể tìm ra một phần tử trung hòa nào khác 0. Phần tử đối cũng như vậy.

Quy tắc giản ước $a + b = a + c \to a + b + (-a) = a + c + (-a)$ mà đây là nhóm giao hoán và (-a) là phần tử đối của a.

Vậy $a + (-a) + b = a + (-a) + c \to 0 + b = 0 + c \to b = c$

Quy tắc giản ước: $x + a = b \to x + a + (-a) = b + (-a) \to x + 0 = x = b + (-a)$

### 3. Cấp của nhóm

Trong toán học, cấp của một nhóm hữu hạn là số phần tử của nhóm đó, nếu nhóm đó có vô số phần tử ta gọi đó là nhóm có cấp vô hạn. Cấp của một phần tử trong nhóm là cấp của nhóm phụ lớn nhất có thể sinh ra được từ phần tử đó. Nếu phép toán của nhóm đó là phép nhân, ta có thể định nghĩa cấp của một phần tử là số $m$ nhỏ nhất thỏa mãn $a ^ m = e$ với e là phần tử trung hòa, m là cấp của phần tử a, $a^m$ là tích của m lần a. Nếu không tồn tại m thỏa mãn ta nói cấp của phần tử a là vô hạn.

Ký hiệu: 
+ Cấp của nhóm G: ord(G) hay |G|
+ Cấp của phần tử a: ord(a) hay |a|

Ngoài ra, theo định lý Lagrange (la gờ răng :L) thì cấp của nhóm phụ hữu hạn thuộc G (nhóm G hữu hạn) thì sẽ luôn chia hết, kiểu ord(G)|ord(a). Từ đó nhóm có bậc là số nguyên tố sẽ chỉ có hai nhóm con cấp 1 và chính nó.

Cũng là ngoài ra, nếu ord(G) = n thì nhóm $|Z_{n}^{*}| = \phi(n)$ với $\phi(n)$ tính theo hàm Euler.


Ví dụ: Nhóm(R, +) ta dễ thấy $|G| = \infty$ vì số thực là vô hạn.


## II. Writes up
