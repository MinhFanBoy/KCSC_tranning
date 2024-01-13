
## RSA_12

---

**_TASK_**

Smallest exponent should be fastest, right?

Challenge files:
  - [salty.py](https://cryptohack.org/static/challenges/salty_9854bdcadc3f8b8f58008a24d392c1bf.py)
  - [output.txt](https://cryptohack.org/static/challenges/output_95f558e889cc66920c24a961f1fb8181.txt)

---

```python


from gmpy2 import iroot
from Crypto.Util.number import *
from factordb.factordb import *

def main():
    txt = open("output.txt", "r").read().split(" ")

    e = 1
    n = txt[2]
    ct = txt[-1][:-1]

    print(long_to_bytes(int(ct)).decode())
    

if __name__ == "__main__":
    main()


```


