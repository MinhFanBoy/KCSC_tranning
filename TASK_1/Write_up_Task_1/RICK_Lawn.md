### Crypto_RSA_Lmao

---

**_TASK:_**
```
n = b'MHgzMDE5NzgzNTMzYjljZWVhNDA5YjkzM2QwMjdlZjMyZTFjYWYwZjE2OWIzYzcwNTVlZTM0Njk1MDA4NGFlN2I2YzU3NGNjN2I4ZmY1Mjc0Nw=='

e = '0x61327'

c = b'MHgxNjdkYTJiMzhhYmRiYjg4N2FmZmM0MDlkNGQzNGQxOTdhMDJmNjJhY2E0YTFjNWM4MTk3YjlhZjlkZWU1NDViNTQ5YjBmNWI3NjI0ZjUzNw=='
```
**_Hint:_**

+ $p - 1 \equiv 0 \pmod{e}$
+ [crypto.stack](https://crypto.stackexchange.com/questions/81949/how-to-compute-m-value-from-rsa-if-phin-is-not-relative-prime-with-the-e/81966#81966)

---

Có $n$ là prime mà $n - 1 \equiv 0 \pmod{e} \quad \to \quad phi = k * e$ nên ta không thể tính $d$. Thay vào đó ta sẽ tính m như sau:
Then, one way to derive the possible plaintexts is to compute:

$$C ^ {d} * L ^ {i} \mod{n}$$

where:

+ $λ = (p − 1) * (q − 1) / gcd(p − 1, q − 1)$
+ $C$ is the ciphertext
+ $d \equiv e^{−1} \pmod{λ/e}$. (This is well defined, as $λ/e$ is an integer which is relatively prime to $e$)
+ $L \equiv k ^ {λ/e} \pmod{n}$ where k is an integer such that L≠1(and any such value L works); most values of kwork
+ $i$ is any integer $0 \leq i < e$

Nhưng do ở đây $n$ là prime nên $\lambda = phi(n) = n - 1$


```python


from Crypto.Util.number import *
from base64 import *
from tqdm import *

n = b'MHgzMDE5NzgzNTMzYjljZWVhNDA5YjkzM2QwMjdlZjMyZTFjYWYwZjE2OWIzYzcwNTVlZTM0Njk1MDA4NGFlN2I2YzU3NGNjN2I4ZmY1Mjc0Nw=='
e = '0x61327'
c = b'MHgxNjdkYTJiMzhhYmRiYjg4N2FmZmM0MDlkNGQzNGQxOTdhMDJmNjJhY2E0YTFjNWM4MTk3YjlhZjlkZWU1NDViNTQ5YjBmNWI3NjI0ZjUzNw=='

n = int(b64decode(n).decode(), 16)
e = int(e, 16)
c = int(b64decode(c).decode(), 16)

lam  = (n - 1)
d = pow(e, -1, lam // e)
l = pow(2, lam // e, n)

for x in tqdm(range(0, e), desc = "Progress"):

    flag = long_to_bytes((pow(c, d, n) * pow(l, x, n)) % n)
    if b"KCSC" in flag :
        print(flag)
        break




```

