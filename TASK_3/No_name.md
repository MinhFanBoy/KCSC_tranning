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
+ Có tính giao hoán: $(a + c) + b = a + (b + c)$ $\forall a, b, c \in R$

Vậy (R, +) là một nhóm Abel.

#### c. Một số tính chất

1. Phần tử trung hòa $e$ là duy nhất.
2. Phần tử đối $x'$ của $x$ là duy nhất.
3. Có quy tắc giản ước: $a ∗ x = a ∗ y \to x = y$
4. Phương trình $x ∗ a = b$ có nghiệm duy nhất $x = b ∗ a'$

Thật vậy, theo ví dụ trên (R, +) ta hoàn toàn không thể tìm ra một phần tử trung hòa nào khác 0. Phần tử đối cũng như vậy.

Quy tắc giản ước $a + b = a + c \to a + b + (-a) = a + c + (-a)$ mà đây là nhóm giao hoán và (-a) là phần tử đối của a.

Vậy $a + (-a) + b = a + (-a) + c \to 0 + b = 0 + c \to b = c$

Quy tắc giản ước: $x + a = b \to x + a + (-a) = b + (-a) \to x + 0 = x = b + (-a)$

### 3. Cấp của nhóm

Trong toán học, cấp của một nhóm hữu hạn là số phần tử của nhóm đó, nếu nhóm đó có vô số phần tử ta gọi đó là nhóm có cấp vô hạn. Cấp của một phần tử trong nhóm là cấp của nhóm phụ lớn nhất có thể sinh ra được từ phần tử đó. Nếu phép toán của nhóm đó là phép nhân, ta có thể định nghĩa cấp của một phần tử là số $m$ nhỏ nhất thỏa mãn $a ^ m = e$ với e là phần tử trung hòa, m là cấp của phần tử a, $a^m$ là tích của m lần a. Nếu không tồn tại m thỏa mãn ta nói cấp của phần tử a là vô hạn.

Ký hiệu: 
+ Cấp của nhóm G: ord(G) hay |G|
+ Cấp của phần tử a: ord(a) hay |a|

Ngoài ra, theo định lý Lagrange (la gờ răng :L) thì cấp của nhóm phụ hữu hạn thuộc G (nhóm G hữu hạn) thì sẽ luôn chia hết, kiểu ord(a)|ord(G). Từ đó nhóm có bậc là số nguyên tố sẽ chỉ có hai nhóm con cấp 1 và chính nó.

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

F***! Bài này hơi lừa. Khi kết nối đến server ,hệ thống cho 1 bộ khóa công khai của Alice, sau đó ta có thệ tạo với Bob một cặp khóa với g, p, a do ta chọn. Khi gửi khóa công Khai của Alice, Bob sẽ gửi lại khóa Công khai của anh ta B .Khi chúng ta gửi cho Bob giá trị của khóa công khai của Alice với g = A . Bob sau đó sẽ tính toán và gửi cho chúng ta bí mật được chia sẻ.

Có một vài cách giải khá hay nên tìm hiểu thêm. Cách giải mình sử dụng là gửi A cho Bob, từ đó nhận được.$A ^ b \pmod{p} = $secret. Nhưng secret ở đây chưa được mod p nên nhớ mod vào.

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
        return unpad(plaintext, 16)
    else:
        return plaintext
# socket.cryptohack.org 13373

s = remote("socket.cryptohack.org", 13373)

s.recv()

public_key = loads(s.recvline())

s.recvuntil(b":")

Bob_key_1 = loads(s.recvuntil(b"}"))

s.recvuntil(b":")

dict_1 = loads(s.recvuntil(b"}"))

s.recv()

tmp = {}

tmp["p"] = public_key["p"]

tmp["g"] = public_key["A"]
tmp["A"] = "0x01"
s.send(dumps(tmp).encode())

s.recvuntil(b":")

Bob_key_2 = loads(s.recvuntil(b"}"))
s.recvuntil(b":")

dict_2 = loads(s.recvuntil(b"}"))

shared_secret = int(Bob_key_2["B"], 16) % int(public_key["p"], 16)
iv = dict_1["iv"]
ciphertext = dict_1["encrypted"]

print(f"This is flag: {decrypt_flag(shared_secret, iv, ciphertext)}")

```

> crypto{n07_3ph3m3r4l_3n0u6h}

### 9. Additive

---

**_TASK:_**

Alice and Bob decided to do their DHKE in an additive group rather than a multiplicative group. What could go wrong?

Use the script from "Diffie-Hellman Starter 5" to decrypt the flag once you've recovered the shared secret.

Connect at socket.cryptohack.org 13380

---

Sau khi tìm hiểu (copy code) mình thấy:
+ $A = g * a \pmod{p}$
+ $B = g * b \pmod{p}$
+ secret = $g * a * b \pmod{p}$

+ $\to a = A * g ^ {-1} \pmod{p}$
+ $\to b = B * g ^ {-1} \pmod{p}$
+ $\to \text{secret} = g ^ {-1} * A * B\pmod{p}$

Áp dụng đúng công thức trên là ta có flag.

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
        return unpad(plaintext, 16)
    else:
        return plaintext
# socket.cryptohack.org 13380

s = remote("socket.cryptohack.org", 13380)

s.recv()

public = loads(s.recvline())

s.recvuntil(b": ")

key = loads(s.recvline())

s.recvuntil(b": ")

tmp = loads(s.recvline())

shared_secret = int(public["A"], 16) * int(key["B"], 16) * pow(2, -1, int(public["p"], 16)) % int(public["p"], 16)
iv = tmp["iv"]
ciphertext = tmp["encrypted"]

print(f"This is flag: {decrypt_flag(shared_secret, iv, ciphertext)}")

```

> crypto{cycl1c_6r0up_und3r_4dd1710n?}

### 10. Static Client 2

---

**_TASK:_**

Bob got a bit more careful with the way he verifies parameters. He's still insisting on using the p and g values provided by his partner. Wonder if he missed anything?

Connect at socket.cryptohack.org 13378

---

Bài này có vẻ giống bài trên nhưng nó đã chặn một số đầu vào. Ta tiến hành google để osint flag.

Ta đi tìm số smooth prime với điều kiện smooth_pime > p. Vì smooth prime sẽ giúp chúng ta có thể tính được discrete_log từ đó tìm ra b.

Có:
+ $2 ^ a = A \pmod{p}$
+ $2 ^ b = B' \pmod{p'}$

Do p' là smooth prime nên ta có thể tìm ra b. Từ đó có secret = $A ^ b$ ra flag.

Nói thêm một tý, smooth prime (gọi là p) là số khi (p - 1) không  là số nguyên tố và có các số nguyên tố sau khi phân tách nhỏ.

```py


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from pwn import *
from json import *
from Crypto.Util.number import *
from factordb.factordb import FactorDB
from sympy.ntheory.residue_ntheory import *

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
    
def smooth_prime(p: int) -> int:
    mul = 1
    i = 1
    
    while (mul + 1).bit_length() <= p.bit_length() or not isPrime(mul + 1):
        mul *= i
        i += 1
    return mul + 1

    
# socket.cryptohack.org 13378

s = remote("socket.cryptohack.org", 13378)

s.recv()

public = loads(s.recvline())

s.recvuntil(b": ")

Bob_key = loads(s.recvline())

s.recvuntil(b": ")

dict_1 = loads(s.recvline())



s.recv()


tmp = {}

p = int(public["p"], 16)



tmp["p"] = hex(smooth_prime(p))

tmp["g"] = "0x02"
tmp["A"] = public["A"]
s.send(dumps(tmp).encode())

s.recv()
s.recv()


Bob_key_2 = loads(s.recvline())

s.recvuntil(b": ")

dict = loads(s.recvline())


shared_secret = pow(int(public["A"], 16), discrete_log(int(tmp["p"], 16), int(Bob_key_2["B"], 16), 2), p)
iv = dict_1["iv"]
ciphertext = dict_1["encrypted"]

print(f"This is flag: {decrypt_flag(shared_secret, iv, ciphertext)}")

```

### 11. Script Kiddie

---

**_TASK:_**

Found this cool script on Github and I've been using it to keep my secrets from anyone listening in on the school wifi!

Challenge files:
  - script.py
  - output.txt

**_FILE:_**

```py

from Crypto.Cipher import AES
import hashlib
import secrets


def header():
    print("""  _____  _  __  __ _
 |  __ \(_)/ _|/ _(_)
 | |  | |_| |_| |_ _  ___
 | |  | | |  _|  _| |/ _ \
 | |__| | | | | | | |  __/
 |_____/|_|_| |_| |_|\___|
 | |  | |    | | |
 | |__| | ___| | |_ __ ___   __ _ _ __
 |  __  |/ _ \ | | '_ ` _ \ / _` | '_ \
 | |  | |  __/ | | | | | | | (_| | | | |
 |_|  |_|\___|_|_|_| |_| |_|\__,_|_| |_|

                                        """)


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def pkcs7_unpad(message, block_size=16):
    if len(message) == 0:
        raise Exception("The input data must contain at least one byte")
    if not is_pkcs7_padded(message):
        return message
    padding_len = message[-1]
    return message[:-padding_len]


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
    return pkcs7_unpad(plaintext).decode('ascii')


def generate_public_int(g, a, p):
    return g ^ a % p


def generate_shared_secret(A, b, p):
    return A ^ b % p


def goodbye():
    print('Goodbye!')


def main():
    header()
    print('[-] Collecting data from Alice')
    p = int(input('> p: '))
    q = (p - 1) // 2
    g = int(input('> g: '))
    A = int(input('> A: '))
    print('[+] All data collected from Alice')

    print('[+] Generating public integer for alice')
    b = secrets.randbelow(q)
    B = generate_public_int(g, b, p)
    print(f'[+] Please send the public integer to Alice: {B}')
    print('')
    input('[+] Press any key to continue')
    print('')

    print('[+] Generating shared secret')
    shared_secret = generate_shared_secret(A, b, p)

    query = input('Would you like to decrypt a message? (y/n)\n')
    if query == 'y':
        iv = input('[-] Please enter iv (hex string)\n')
        ciphertext = input('[-] Please enter ciphertext (hex string)\n')
        flag = decrypt_flag(shared_secret, iv, ciphertext)
        print(f'[+] Flag recovered: {flag}')
        goodbye()
    else:
        goodbye()


if __name__ == '__main__':
    main()
```

**_Output:_**

```py
p: 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
g: 2
A: 539556019868756019035615487062583764545019803793635712947528463889304486869497162061335997527971977050049337464152478479265992127749780103259420400564906895897077512359628760656227084039215210033374611483959802841868892445902197049235745933150328311259162433075155095844532813412268773066318780724878693701177217733659861396010057464019948199892231790191103752209797118863201066964703008895947360077614198735382678809731252084194135812256359294228383696551949882
B: 652888676809466256406904653886313023288609075262748718135045355786028783611182379919130347165201199876762400523413029908630805888567578414109983228590188758171259420566830374793540891937904402387134765200478072915215871011267065310188328883039327167068295517693269989835771255162641401501080811953709743259493453369152994501213224841052509818015422338794357540968552645357127943400146625902468838113443484208599332251406190345653880206706388377388164982846343351
iv: 'c044059ae57b61821a9090fbdefc63c5'
encrypted_flag: 'f60522a95bde87a9ff00dc2c3d99177019f625f3364188c1058183004506bf96541cf241dad1c0e92535564e537322d7'
```

---

Khi nhìn vào file đề cho mình thấy nó đang hơi sai:

      def generate_public_int(g, a, p):
          return g ^ a % p
      
      
      def generate_shared_secret(A, b, p):
          return A ^ b % p


Nó trong python là tính xor chứ không phải mũ. Nên từ đó ta thấy $A = g \oplus a \text{và} B = g \oplus b \text{ nên từ đó ta có } \text{secret} = A \oplus B \oplus g$. Sau khi có secret ta chỉ cần giải mã bằng hàm có sẵn là được.

```py


from Crypto.Cipher import AES
import hashlib
import secrets

p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
g = 2
A = 539556019868756019035615487062583764545019803793635712947528463889304486869497162061335997527971977050049337464152478479265992127749780103259420400564906895897077512359628760656227084039215210033374611483959802841868892445902197049235745933150328311259162433075155095844532813412268773066318780724878693701177217733659861396010057464019948199892231790191103752209797118863201066964703008895947360077614198735382678809731252084194135812256359294228383696551949882
B = 652888676809466256406904653886313023288609075262748718135045355786028783611182379919130347165201199876762400523413029908630805888567578414109983228590188758171259420566830374793540891937904402387134765200478072915215871011267065310188328883039327167068295517693269989835771255162641401501080811953709743259493453369152994501213224841052509818015422338794357540968552645357127943400146625902468838113443484208599332251406190345653880206706388377388164982846343351
iv = 'c044059ae57b61821a9090fbdefc63c5'
encrypted_flag = 'f60522a95bde87a9ff00dc2c3d99177019f625f3364188c1058183004506bf96541cf241dad1c0e92535564e537322d7'

shared_secret = A ^ B ^ g

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def pkcs7_unpad(message, block_size=16):
    if len(message) == 0:
        raise Exception("The input data must contain at least one byte")
    if not is_pkcs7_padded(message):
        return message
    padding_len = message[-1]
    return message[:-padding_len]


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
    return pkcs7_unpad(plaintext).decode('ascii')

print(decrypt_flag(shared_secret, iv, encrypted_flag))

```

### 12. The Matrix

---

**_TASK:_**

I must get out of here. I must get free, and in this mind is the key, my key!

Challenge files:
  - the_matrix.sage
  - flag.enc

**_FILE:_**

```py

import random

P = 2
N = 50
E = 31337

FLAG = b'crypto{??????????????????????????}'

def bytes_to_binary(s):
    bin_str = ''.join(format(b, '08b') for b in s)
    bits = [int(c) for c in bin_str]
    return bits

def generate_mat():
    while True:
        msg = bytes_to_binary(FLAG)
        msg += [random.randint(0, 1) for _ in range(N*N - len(msg))]

        rows = [msg[i::N] for i in range(N)]
        mat = Matrix(GF(2), rows)

        if mat.determinant() != 0 and mat.multiplicative_order() > 10^12:
            return mat

def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row)) for row in data.splitlines()]
    return Matrix(GF(P), rows)

def save_matrix(M, fname):
    open(fname, 'w').write('\n'.join(''.join(str(x) for x in row) for row in M))

mat = generate_mat()

ciphertext = mat^E
save_matrix(ciphertext, 'flag.enc')

```

**_OUTPUT:_**

```txt
00000001111101100001101010010001001011000110001001
10111010010100110001011011111110011000001001000001
01011101000110110101010100100100111110110110011111
11101100011011010001111011011000100010110001001010
11111111101001010101001011111101010010011010101001
10010011101000000010000110100101111011110011101110
00011100010011010110000000001011000111010101001011
01001111000110100111110011000101011110010111111110
01111001110011000100000110010101011111010000000011
11001101010111111011110110101010001101001001111101
01100111000100010101000001011011001101001110101000
00010001001011101111100010101101011000101100010111
01101100101101011101101000110001011111111010000100
00001110111111000111111100011110000101100100000011
10001001111111011000111011111010110111111111000110
01111101100011110110111000011110000100111001110100
11111100110101111001111000110100011010111011110001
00100011011100101010111011111100000010000101111111
01111001110100011111011100100011011010010011111000
01011011101011111111101011011011000111110011111010
00010100110111110011111100111101100000001101110111
10011011011101110101100110110000011101000010101011
01111000001111011011111000100010010010010111101001
00100000010001110000001101111100011111110011011000
10010101101011011111101111101000111010010011111001
10011011000111000001010111011000000000100111100011
11001001010001111111000011011011101001101010001000
00100100000101110010001001011001111011001110100001
00000101000101100111010111101010001101111110011001
00101000011010100110100111111110000101011001011110
11011001001111111010000001100111011101101100110110
00111000011011011111111011110001001101001101101100
11110010101001100110000110110000100000101010101011
00101001000011001110110111100010010011100101001000
11000100010010111110110010100110110110101000110110
01101011000111001111011110000110001011111000011100
11010011001111111110100101100011000000000011110001
10000011000101100011000110111111011010110111101000
11000011000100010001001011010011010000001101100011
11011001111001010100010101001100001010101100010010
10110101010111111010110001111111100100110001001100
11101001100110001001001100000011100101001010011010
10000011100110001101010110010010100001010011011101
10001110111111100110011000010000011011011111011001
00011100011111110101011100111000110010100011000010
00111111010010111100100101100001001011110101111100
10000100101101000011011010100100011111100101101111
00011101110001001010111001111011111110110011011001
11111100110101111100110001011001000001111100110011
00110010110110011001001111110110000011001111010110
```

---

Sau khi đọc đề ta thấy, (M là ma trận ban đầu), ta có ma trân M ^ E, nên bây giờ ta cần tìm lại M (vì các bit đầu của M là bit của flag). Nên ta ta tìm $a =  E ^ {-1} \pmod{mat.multiplicative_order()}$ khi đó $(M ^ E) ^ {a} = M ^ {E * a} = M$.

với mat.multiplicative_order() là hàm tìm cấp của ma trận trong phép nhân tức tìm b sao cho $M ^ b = I$ với i là ma trận đơn vị, M là ma trận ta cho.

```sage


E = 31337

msg = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0], [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0]]

msg = Matrix(GF(2), msg)

msg ^= pow(E, -1, msg.multiplicative_order())

msg = [list(x) for x in msg]

print(msg)

rows = "".join([msg[i::50] for i in range(50)])
for x in range(1,len(msg)):
    print(long_to_bytes(int(rows[:x], 2)))
```

```py


from Crypto.Util.number import *

N = 50
msg = [[int(y) for y in x] for x in open("flag.enc", 'r').read().split("\n")]

msg = [[0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]]

msg = [[str(y) for y in x] for x in msg]

tmp = []

for x in msg:
    tmp += x
msg = "".join(tmp)

print(f"msg = {msg}")
rows = "".join([msg[i::N] for i in range(N)])

print(long_to_bytes(int(rows[:len("crypto{??????????????????????????}") * 8], 2)))

```
