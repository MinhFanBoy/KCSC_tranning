
### Crypto

---

**_TASK:_**

Here's my token signing and verification server. I'm not sure it's doing signing properly, but I've implemented some safeguards to ensure it won't hand out admin tokens to just anyone.

Connect at socket.cryptohack.org 13376

Challenge files:
  - [13376.py](https://cryptohack.org/static/challenges/13376_f33b73edaadf6e553906fb0fc2b79385.py)

---

Bài này cho ta mã hóa bằng d của mọi tin nhắn ta gửi(đương nhiên trừ token :>). Vậy nên mình nhân vào token một số rồi chia lại cho nó là ta sẽ có flag ban đàu và qua mặt dc source, để dễ hiểu thì nó như sau:
$$m ^ d = c \pmod{n}$$
$$(80 * m) ^ {d} \equiv c_1$$
$$(80 ) ^ {d} \equiv c_2$$
$$\to c_1 / c_2 = (80 * m) ^ d / 80 ^ d = (80 / 80 * m) ^ d = m ^ d \pmod{n}$$
từ đó ta có c nên chỉ cần gửi nữa là xong :).
```py

from pwn import *
from json import *
from Crypto.Util.number import *

# socket.cryptohack.org 13376

s = connect("socket.cryptohack.org", "13376")
print(s.recv().decode())

def get_publickey() -> tuple:
    tmp = {"option":"get_pubkey"}
    s.send(dumps(tmp).encode())
    a = loads(s.recv())
    return int(a["N"], 16), int(a["e"], 16)

def send_msg(msg: str) -> str:
    tmp = {"option":"sign", "msg" : str(hex(bytes_to_long(msg))[2:])}

    s.send(dumps(tmp).encode())
    a = loads(s.recv())
    return  int(a["signature"], 16)

def check(msg: str, signature):
    tmp = {"option" : "verify", "msg" : str(hex(bytes_to_long(msg))[2:]), "signature" : signature}
    
    s.send(dumps(tmp).encode())
    a = loads(s.recv())
    return a

msg = b"admin=True"
N, e = get_publickey()

enc_1 = send_msg(long_to_bytes(bytes_to_long(b"admin=True") * 80))
enc_2 = send_msg(long_to_bytes(80))

enc = pow(enc_1 * pow(enc_2, -1, N), 1, N)

print(check(b"admin=True", hex(enc)))



```
