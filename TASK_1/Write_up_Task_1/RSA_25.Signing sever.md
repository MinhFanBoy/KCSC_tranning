### Crypto

---

**_TASK:_**

Let's Decrypt80 pts · 828 Solves
If you can prove you own CryptoHack.org, then you get access to one of our secrets.

Connect at socket.cryptohack.org 13391

Challenge files:
  - 13391.py

---


```py

from pwn import *
from json import *
from Crypto.Util.number import *

# socket.cryptohack.org 13374

s = connect('socket.cryptohack.org', 13374)

print(s.recv().decode())

dict = {"option": "get_pubkey"}
s.send(dumps(dict).encode())
tmp = loads(s.recv())

N = int(tmp["N"], 16)
e = int(tmp["e"], 16)
dict = {"option": "get_secret"}
s.send(dumps(dict).encode())
tmp = loads(s.recv().decode())
enc = int(tmp["secret"], 16)


print(f"{N = }")
print(f"{e = }")
print(f"{enc = }")


dict = {"option": "sign", "msg": hex(enc)}
s.send(dumps(dict).encode())
tmp = loads(s.recv().decode())
print(long_to_bytes(int(tmp["signature"], 16)))


```
