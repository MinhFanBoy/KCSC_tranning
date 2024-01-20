
### Crypto

---

**_TASK:_**



```python

from Crypto.Util.number import *
from Crypto.Cipher import AES
import os
from flag import FLAG

def pad(data):
    padding_size = (16 - (len(data) % 16)) % 16    
    padded_data = data.ljust(len(data) + padding_size, b'\x00')
    return padded_data

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p*q
d = getRandomInteger(64)
key = long_to_bytes(2024*p + d)[:16]
iv = os.urandom(16)
flag = pad(FLAG)
cipher = AES.new(iv,AES.MODE_CBC,key)
c = bytes_to_long(cipher.encrypt(flag))

val = (2*p**3 + 3*p**2) % n

print('n=' + str(n))
print('iv='+str(iv))
print('c=' + str(c))
print('val=' + str(val))

```
---

Ở đây ta dễ thấy $val \equiv 2 * p ^ 3 + 3 * p ^ 2 \pmod{n} \quad \to \quad val = p ^2 * (2 * p + 3) \pmod{n}$, mà $n = p * q$ nên từ đó ta có $gcd(val, n) = p$. Do $2024 * p >> random(64)$ mà key chỉ lấy có 16 bytes đầu của nó nên ở đây d trở nên vô dụng, từ đó ta dễ dàng có được key và hoàn thành thử thách.

```
n=116422885145248934225686914429146707250914314074098936204837356406828626206897073267773920624624570359557096258952933379700970822531971353624244003807545840017125763493920463202691952331937661437791742467140169441129657049404630272768006776625873529380414431191459118716479168976156074571723572848577917978433
iv=b':\x88(\x7fPK\xba+\x83G\xd9+\xb4:w\x02'
c=26003470241248183886366385521067853859993513649868770030402657395420294707645314821746877611126190234881774517848630
val=7728896068211597749662327611345565126580093002981776126298758158041181358825984746690714615330702804921437965445589537359948914406962280207495027174049984054166471642458821726259288576073467035129599467101913206457949501633692562613026832767483110632244571322446440661984724942084414921153978748727244489994

p = GCD(val,n)
key  = long_to_bytes(2024*p)[:16]
cipher = AES.new(iv,AES.MODE_CBC,key)
flag = cipher.decrypt(long_to_bytes(c))
print(flag)
```
