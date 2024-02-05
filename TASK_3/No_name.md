
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
