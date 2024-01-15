
### crypto

---

**_TASK:_**

I need to produce millions of RSA keys quickly and the standard way just doesn't cut it. Here's yet another fast way to generate primes which has actually resisted years of review.

Challenge files:
  - fast_primes.py
  - key.pem
  - ciphertext.txt

---


```python


from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB
from Crypto.Cipher import PKCS1_OAEP

c = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28

txt = open('key.pem', 'r').read()

n = vars(RSA.importKey(txt))
e = int(n['_e'])
n = int(n['_n'])
print(n)
print(c)
f = FactorDB(n)
f.connect()
p, q = f.get_factor_list()
print(p, q)

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
key = RSA.construct((n, e, d))

cipher = PKCS1_OAEP.new(key)
print(cipher.decrypt(long_to_bytes(c)))



```
