
## RSA_13

---

**_TASK_**

My primes should be more than large enough now!

Challenge files:
  - modulus_inutilis.py
  - output.txt

---

```python


from gmpy2 import iroot
from Crypto.Util.number import *

def main():
    txt = open("output.txt", "r").read().split("\n")
    ct = int(txt[2][5:])
    print(long_to_bytes(iroot(ct, 3)[0]).decode())

    

if __name__ == "__main__":
    main()


```
