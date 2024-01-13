
## RSA_10

---

**_TASK_**

It was taking forever to get a 2048 bit prime, so I just generated one and used it twice.

 If you're stuck, look again at the formula for Euler's totient.
Challenge files:
  - [output.txt](https://cryptohack.org/static/challenges/output_00dace150c0bc52f7abf03fc3e9529d2.txt)

---

```python


from gmpy2 import iroot
from Crypto.Util.number import *

def main():
    txt = open("output.txt", "r").read().split("\n")

    n = int(txt[0][4:])
    e = 65537
    ct = int(txt[2][5:])
    
    prime = iroot(n, 2)[0]

    assert prime ** 2 == n

    phi = prime * (prime - 1)

    print(long_to_bytes(pow(ct, pow(e, -1, phi), n)).decode())

if __name__ == "__main__":
    main()


```
