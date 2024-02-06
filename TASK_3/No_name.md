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

### 3. Diffie-Hellman Starter 3

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

### 4. Diffie-Hellman Starter 4

---

**_TASK:_**

Now it's time to calculate a shared secret using data received from your friend Alice. Like before, we will be using the NIST parameters:

g: 2

p: 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

You have received the following integer from Alice:

A: 70249943217595468278554541264975482909289174351516133994495821400710625291840101960595720462672604202133493023241393916394629829526272643847352371534839862030410331485087487331809285533195024369287293217083414424096866925845838641840923193480821332056735592483730921055532222505605661664236182285229504265881752580410194731633895345823963910901731715743835775619780738974844840425579683385344491015955892106904647602049559477279345982530488299847663103078045601

You generate your secret integer b and calculate your public one B, which you send to Alice.

b: 12019233252903990344598522535774963020395770409445296724034378433497976840167805970589960962221948290951873387728102115996831454482299243226839490999713763440412177965861508773420532266484619126710566414914227560103715336696193210379850575047730388378348266180934946139100479831339835896583443691529372703954589071507717917136906770122077739814262298488662138085608736103418601750861698417340264213867753834679359191427098195887112064503104510489610448294420720

B: 518386956790041579928056815914221837599234551655144585133414727838977145777213383018096662516814302583841858901021822273505120728451788412967971809038854090670743265187138208169355155411883063541881209288967735684152473260687799664130956969450297407027926009182761627800181901721840557870828019840218548188487260441829333603432714023447029942863076979487889569452186257333512355724725941390498966546682790608125613166744820307691068563387354936732643569654017172

You and Alice are now able to calculate a shared secret, which would be infeasible to calculate knowing only {g,p,A,B}.

What is your shared secret?

---

Bài này mình sử dụng công thức của bài trên, do đã biết A và có b nên ta sẽ dễ dàng tính secret = $A ^ b \pmod{q}$ và hoàn thành đáp án.

```py


g = 2

p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919


A = 70249943217595468278554541264975482909289174351516133994495821400710625291840101960595720462672604202133493023241393916394629829526272643847352371534839862030410331485087487331809285533195024369287293217083414424096866925845838641840923193480821332056735592483730921055532222505605661664236182285229504265881752580410194731633895345823963910901731715743835775619780738974844840425579683385344491015955892106904647602049559477279345982530488299847663103078045601

b = 12019233252903990344598522535774963020395770409445296724034378433497976840167805970589960962221948290951873387728102115996831454482299243226839490999713763440412177965861508773420532266484619126710566414914227560103715336696193210379850575047730388378348266180934946139100479831339835896583443691529372703954589071507717917136906770122077739814262298488662138085608736103418601750861698417340264213867753834679359191427098195887112064503104510489610448294420720

B = 518386956790041579928056815914221837599234551655144585133414727838977145777213383018096662516814302583841858901021822273505120728451788412967971809038854090670743265187138208169355155411883063541881209288967735684152473260687799664130956969450297407027926009182761627800181901721840557870828019840218548188487260441829333603432714023447029942863076979487889569452186257333512355724725941390498966546682790608125613166744820307691068563387354936732643569654017172

print(pow(A, b, p))
```


### 5. Diffie-Hellman Starter 5

---

**_TASK:_**

```py
Alice wants to send you her secret flag and asks you to generate a shared secret with her. She also tells you she will be using the NIST standard:

g: 2

p: 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

You receive the following integer from Alice:

A: 112218739139542908880564359534373424013016249772931962692237907571990334483528877513809272625610512061159061737608547288558662879685086684299624481742865016924065000555267977830144740364467977206555914781236397216033805882207640219686011643468275165718132888489024688846101943642459655423609111976363316080620471928236879737944217503462265615774774318986375878440978819238346077908864116156831874695817477772477121232820827728424890845769152726027520772901423784

You then generate your secret integer and calculate your public one, which you send to Alice.

b: 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944

B: 1241972460522075344783337556660700537760331108332735677863862813666578639518899293226399921252049655031563612905395145236854443334774555982204857895716383215705498970395379526698761468932147200650513626028263449605755661189525521343142979265044068409405667549241125597387173006460145379759986272191990675988873894208956851773331039747840312455221354589910726982819203421992729738296452820365553759182547255998984882158393688119629609067647494762616719047466973581

Individually you each use the shared secret to derive an AES private key. This allows you to encrypt large amounts of data over your channel without needing to exchange keys again.

Alice sends you the following IV and ciphertext:

{'iv': '737561146ff8194f45290f5766ed6aba', 'encrypted_flag': '39c99bf2f0c14678d6a5416faef954b5893c316fc3c48622ba1fd6a9fe85f3dc72a29c394cf4bc8aff6a7b21cae8e12c'}

Decrypt this to obtain your flag!
```
---

Bài này khá đơn giản, giống như kiến thức của bài trên. Do ta đã có A,b nên tính secret = $A ^ b \pmodpmod{q}$ là có được flag. Sử dụng file giải mã có sẵn của đề bài sẽ nhanh hơn.

```py

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')




g = 2

p =  2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

A =  112218739139542908880564359534373424013016249772931962692237907571990334483528877513809272625610512061159061737608547288558662879685086684299624481742865016924065000555267977830144740364467977206555914781236397216033805882207640219686011643468275165718132888489024688846101943642459655423609111976363316080620471928236879737944217503462265615774774318986375878440978819238346077908864116156831874695817477772477121232820827728424890845769152726027520772901423784

b = 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944

B = 1241972460522075344783337556660700537760331108332735677863862813666578639518899293226399921252049655031563612905395145236854443334774555982204857895716383215705498970395379526698761468932147200650513626028263449605755661189525521343142979265044068409405667549241125597387173006460145379759986272191990675988873894208956851773331039747840312455221354589910726982819203421992729738296452820365553759182547255998984882158393688119629609067647494762616719047466973581


tmp = {'iv': '737561146ff8194f45290f5766ed6aba', 'encrypted_flag': '39c99bf2f0c14678d6a5416faef954b5893c316fc3c48622ba1fd6a9fe85f3dc72a29c394cf4bc8aff6a7b21cae8e12c'}



shared_secret = pow(A, b, p)
iv = tmp["iv"]
ciphertext = tmp["encrypted_flag"]

print(decrypt_flag(shared_secret, iv, ciphertext))
```
> crypto{sh4r1ng_s3cret5_w1th_fr13nd5}

### 6. Parameter Injection

---

**_TASK:_**

You're in a position to not only intercept Alice and Bob's DH key exchange, but also rewrite their messages. Think about how you can play with the DH equation that they calculate, and therefore sidestep the need to crack any discrete logarithm problem.

Use the script from "Diffie-Hellman Starter 5" to decrypt the flag once you've recovered the shared secret.

Connect at socket.cryptohack.org 13371

---

Bài này sử dụng MITM, đã được nhắc đến từ TASK2(có thể xem lại nếu quên)

A malicious Malory, that has a MitM (man in the middle) position, can manipulate the communications between Alice and Bob, and break the security of the key exchange.

Các bước cảu tấn công man in the middle:

Step 1: Chon public key (g, p) trong đó p là số modulus, g là số base.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/370576d5-e146-40f6-a9ab-f92d7f7ab4d6)

Step 2: Chon privatekey. Let Alice pick a private random number a and let Bob pick a private random number b, Malory picks 2 random numbers c and d.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/392af297-47a1-42cc-9262-73ee41807be9)

Step 3: Intercepting public values,

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/87d2d684-1b2b-4075-b712-24770fb3cb61)

Malory intercepts Alice’s public value $A = g ^ a \pmod{p}$, block it from reaching Bob, and instead sends Bob her own public value $p$ (có thể gửi $g ^ c \pmod{p}$ cũng được với c là số mình chọn), Malory intercepts Bob’s public value $B = g ^ b \pmod{p}$, block it from reaching Alice, and instead sends Alice her own public value $p$

Step 4: Computing secret key

Tính key sai: $S = p ^ a = p ^ b = 0 \pmod{p}$

Từ đó ta có secret = 0.

```py


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from pwn import *
from json import *

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

# socket.cryptohack.org 13371
    
s = connect("socket.cryptohack.org", 13371)

s.recv().decode()
public_key = loads(s.recvuntil(b"}"))

tmp = public_key
tmp["A"] = public_key["p"]


s.recvuntil(b":").decode()

s.send(dumps(tmp).encode())

s.recvuntil(b":").decode()

tmp = loads(s.recvline())

s.recv().decode()


tmp["B"] = public_key["p"]

s.send(dumps(tmp).encode())

s.recvuntil(b":").decode()

tmp = loads(s.recvuntil(b"}"))

shared_secret = 0
iv = tmp["iv"]
ciphertext = tmp["encrypted_flag"]

print(f"This is flag: {decrypt_flag(shared_secret, iv, ciphertext)}")
```

> crypto{n1c3_0n3_m4ll0ry!!!!!!!!}

### 7. Export-grade

---

**_TASK:_**
Alice and Bob are using legacy codebases and need to negotiate parameters they both support. You've man-in-the-middled this negotiation step, and can passively observe thereafter. How are you going to ruin their day this time?

Connect at socket.cryptohack.org 13379

---

Bài này mình sử dụng MITM để làm. Thử thách này mô phỏng cuộc tấn công Logjam khét tiếng trên nhiều giao thức internet như HTTPS, SSH, IPsec, SMTPS và các giao thức dựa trên TLS sử dụng trao đổi khóa Diffie-Hellman. Cuộc tấn công Logjam cho phép kẻ tấn công trung gian hạ cấp các kết nối TLS dễ bị tấn công xuống mật mã cấp xuất 512 bit, vì có một tùy chọn cho khách hàng quay lại khi bài báo được xuất bản để sử dụng cấp độ bảo mật DHE_EXPORT. Không có dấu hiệu nào về bộ mật mã mà máy chủ đã chọn, vì vậy MiTM có thể dễ dàng sửa đổi bộ mật mã của máy khách thành DHE_EXPORT.

Ý tưởng này được sử dụng trong thử thách. Ban đầu, Alice đưa ra một danh sách chứa danh sách các bộ mật mã được hỗ trợ, từ DH1536 đến DH64. Không có gì ngăn cản chúng tôi sửa đổi thông báo này, do đó chúng tôi có thể chọn tùy chọn yếu nhất trong danh sách, đó là DH64. Sau đó, quá trình trao đổi khóa thông thường được thực hiện và chúng tôi nhận được thông tin về g, p, A, B và iv, mã hóa_flag được tạo từ bí mật chung.

Một giải pháp khác là sử dụng thuật toán Pohlig-Hellman. Số nguyên tố yếu (chúng ta luôn có thể xem FactorDB) và do đó con số sẽ trơn tru. Hoặc chúng ta có thể bỏ qua tất cả công việc này và sử dụng chức năng discrete_log do Sage cung cấp.
​
```py


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from pwn import *
from json import *
from sage.all import *

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16)
    else:
        return plaintext

# socket.cryptohack.org 13379
"""    
s = connect("socket.cryptohack.org", 13379)

print(s.recv())

public_key = loads(s.recvline())

print(s.recv())

s.send(dumps({'supported': ['DH64']}).encode())

print(s.recv())

B = loads(s.recvline())

s.send(dumps(B).encode())

print(s.recv())
print(s.recv())
print(s.recv())

"""
dict = {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x8ec01998f435699b","B": "0xc6302eb03e9f60cf", "iv": "5050ae8ba228bce32488e24cfde43ba9", "encrypted_flag": "4070080abe7edb188368dd0cc6e4af1833619f821b34dc9ce139a3d187741f65"}

g = Mod(int(2), int(dict["p"], 16))
A = Mod(int(dict["A"], 16), int(dict["p"], 16))

a = discrete_log(A, g)

a = 3390858232315700143

shared_secret = pow(int(dict["B"], 16), a, int(dict["p"], 16))
iv = dict["iv"]
ciphertext = dict["encrypted_flag"]

print(f"This is flag: {decrypt_flag(shared_secret, iv, ciphertext)}")
```

> crypto{d0wn6r4d35_4r3_d4n63r0u5}

### 8. Static Client

---

**_TASK:_**

You've just finished eavesdropping on a conversation between Alice and Bob. Now you have a chance to talk to Bob. What are you going to say?

Connect at socket.cryptohack.org 13373

---
