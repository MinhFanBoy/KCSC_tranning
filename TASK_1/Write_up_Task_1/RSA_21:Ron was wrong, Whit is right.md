
### RSA_21

---
**_TASK:_**

Here's a bunch of RSA public keys I gathered from people on the net together with messages that they sent.

As excerpt.py shows, everyone was using PKCS#1 OAEP to encrypt their own messages. It shouldn't be possible to decrypt them, but perhaps there are issues with some of the keys?

Challenge files:
  - excerpt.py
  - keys_and_messages.zip

---

```python



from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB
from Crypto.Cipher import PKCS1_OAEP

c = open('21.ciphertext', 'r').read()
c = int(c, 16)
txt = open('21.pem', 'r').read()
n = vars(RSA.importKey(txt))
e = int(n['_e'])
n = int(n['_n'])

f = FactorDB(n)
f.connect()
p, q = f.get_factor_list()


phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
key = RSA.construct((n, e, d))

cipher = PKCS1_OAEP.new(key)
print(cipher.decrypt(long_to_bytes(c)))




```
