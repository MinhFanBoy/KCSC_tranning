
## RSA6

---

**_Descriptions:_**

Trên thực tế các tin nhắn mỗi khi được mã hóa sẽ được gửi đi kèm với cả bản rõ được hash để xác nhận. Các bước như sau:
  + B1: mã hóa tin nhắn c = m^e (mod n)
  + B2: sử dụng hàm băm cho m (với hàm băm thì thường dc chọn là md5, sha 256 vì nó có tính vảo mật cao và dễ tiếp cận)
  + B3 s = ( H(m) )^d (mod n)
  + B4: Gửi cả cặp (c, s)

Dễ thấy do s = (H(m))^d (mod n) nên ta có thể tính H(m) = s^e mod n. Sử sụng kết quả m = c^d (mod n) nếu H(m) == h(m) thì đây là tin nhắn đúng.

**_Task_**

Sign the flag crypto{Immut4ble_m3ssag1ng} using your private key and the SHA256 hash function.

Challenge files:
  - [private.key](https://cryptohack.org/static/challenges/private_0a1880d1fffce9403686130a1f932b10.key)

---


```python


from factordb.factordb import FactorDB
from Crypto.Util.number import *
from hashlib import sha256


def main():
    flag = "crypto{Immut4ble_m3ssag1ng}"
    hash = bytes_to_long(flag.encode())

    hash_func = sha256()
    hash_func.update(flag.encode())

    txt = open("private", "r").read().split("\n")
    N = txt[0][4:]
    d = txt[1][4:]
    enc = pow(int(hash_func.hexdigest(), 16), int(d), int(N))

    print("enc:", enc)

if __name__ == "__main__":
    main()



```
