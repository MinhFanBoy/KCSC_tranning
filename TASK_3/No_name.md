Tables of contens
=================
* [I. Tổng quát](#i-Tổng-quát)
   * [1. Group](##1-Group)
   * [2. Tính chất](##2-Tính-chất)
* [II. Write up](#ii-Writes-up)


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

### 1. Diffie-Hellman Starter 1

---

**_TASK:_**

The set of integers modulo n, together with the operations of both addition and multiplication is a ring. This means that adding or multiplying any two elements in the set returns another element in the set.

When the modulus is prime: n = p, we are guaranteed an inverse of every element in the set, and so the ring is promoted to a field. We refer to this field as a finite field Fp.

The Diffie-Hellman protocol works with elements of some finite field Fp, where the prime modulus is typically a large prime.

Given the prime p = 991, and the element g = 209, find the inverse element d such that g * d mod 991 = 1.

---

Bài này yêu cầu ta tìm d sao cho $209 * d \equiv 1 \pmod{991}$. Nên mình chuyển vế $d \equiv 209 ^ {-1} \pmod{991}$. Từ đó dễ dàng có được đáp án.

`print(pow(209, -1, 991))`

> 569

### 2. Diffie-Hellman Starter 2

---

**_TASK:_**

Every element of a finite field Fp can be used to make a subgroup H under repeated action of multiplication. In other words, for an element g: H = {g, g^2, g^3, ...}

A primitive element of Fp is an element whose subgroup H = Fp, i.e., every element of Fp, can be written as g^n mod p for some integer n. Because of this, primitive elements are sometimes called generators of the finite field.

For the finite field with p = 28151 find the smallest element g which is a primitive element of Fp.

This problem can be solved by brute-force, but there's also clever ways to speed up the calculation.

---

Bài này nói chung có nhiều cách làm(nhiều cách khá hay nên đọc thêm).

C1: Mình chủ yếu dựa vào tính chất của nó khi mũ tạo ra các phần tử khác nhau để tạo nên một nhóm phụ mới có p - 1 phần tử.

Theo định lý Fermat nhỏ $x ^ {\phi(n)} = xx \pmod{n}$ nên với mọi mũ lớn hơn phi n đều bị lặp lại nên bỏ đi để giảm thời gian tính.

Từ đó nếu trong khoảng [0, phi] mà $a ^ {x} = a \pmod{n}$ khiến con sẽ bị mất đi một phần tử vì a, 1 đều có chung một giá trị (?) trong mod p nên từu đó điều kiện là phần tử sinh không được thỏa mãn.

```py

p = 28151

def find(x):
    for y in range(2, p):
        if pow(x, y, p) == x:
            return False
    return True

for x in range(2, p):
    if find(x):
        print(f"Find: {x}")
        exit()
```

C2:

Cách này dựa vào định lý trong trường:

Nếu p > 2 là prime, $a \in Z_{p}^{*}$ khiến $a ^ {(p - 1)/q} \neq -1 \forall q|(p - 1)$. Nói tóm lại a là phần tử sinh nếu cái lằng nhằng kia khác -1 với mọi q là số nguyên tố chia hết cho (p - 1)

```py


from factordb.factordb import FactorDB

p = 28151

t = FactorDB(p - 1)
t.connect()
tmp = [(p - 1) // x for x in t.get_factor_list()]

def find(k: int) -> bool:
    for i in tmp:
        if pow(k, i, p) == 1:
            return False
    return True

for x in range(2, p):
    if find(x):
        print(x)
        exit()
```

### 3

---

**_TASK:_**

The Diffie-Hellman protocol is used because the discrete logarithm is assumed to be a "hard" computation for carefully chosen groups.

The first step of the protocol is to establish a prime p and some generator of the finite field g. These must be carefully chosen to avoid special cases where the discrete log can be solved with efficient algorithms. For example, a safe prime p = 2*q +1 is usually picked such that the only factors of p - 1 are {2,q} where q is some other large prime. This protects DH from the Pohlig–Hellman algorithm.

The user then picks a secret integer a < p and calculates g^a mod p. This can be transmitted over an insecure network and due to the assumed difficulty of the discrete logarithm, the secret integer should be infeasible to compute.

Given the NIST parameters:

g: 2

p: 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

Calculate the value of g^a mod p for

a: 972107443837033796245864316200458246846904598488981605856765890478853088246897345487328491037710219222038930943365848626194109830309179393018216763327572120124760140018038673999837643377590434413866611132403979547150659053897355593394492586978400044375465657296027592948349589216415363722668361328689588996541370097559090335137676411595949335857341797148926151694299575970292809805314431447043469447485957669949989090202320234337890323293401862304986599884732815


---

Bài này nói về Diffie-hellman là phương thức trao đổi khóa công khai an toàn.

Chọn hai số publickey (g, p), privatekey (a, b) trong đó mỗi bên giữ a hoặc b cẩn thận không để bị lộ hoặc cũng không để đối phương có thể biết privatekey của mình.

Tính:

$A = g ^ a \pmod{p}$

$B = g ^ b \pmod{p}$

sau đó gửi A, B cho đối phương.

secret = $A ^ b = B ^ a = g ^ {a * b} \pmod{p}$

Ở trong bài này ta chỉ cần tính $g ^ a \pmod{p}$ là xong

```py


g =  2

p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

a = 972107443837033796245864316200458246846904598488981605856765890478853088246897345487328491037710219222038930943365848626194109830309179393018216763327572120124760140018038673999837643377590434413866611132403979547150659053897355593394492586978400044375465657296027592948349589216415363722668361328689588996541370097559090335137676411595949335857341797148926151694299575970292809805314431447043469447485957669949989090202320234337890323293401862304986599884732815

print(pow(g, a, p))
```
