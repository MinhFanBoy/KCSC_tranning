
## RSA_8

---

**_TASK_**

Here is my super-strong RSA implementation, because it's 1600 bits strong it should be unbreakable... at least I think so!

Challenge files:
  - [inferius.py](https://cryptohack.org/static/challenges/inferius_e85eea9b19cd68aa71ce850918302bad.py)
  - [output.txt](https://cryptohack.org/static/challenges/output_4b843d94b6196df152219c3165b9347f.txt)

---

```python


from factordb.factordb import *
from Crypto.Util.number import *

def main():
    txt = open("output.txt", "r").read().split("\n")

    n = int(txt[0][4:])
    e = 3
    ct = int(txt[2][5:])

    primes = FactorDB(n)
    primes.connect()
    lst = primes.get_factor_list()

    phi = (lst[0] - 1) * (lst[1] - 1)

    print(long_to_bytes(pow(ct, pow(e, -1, phi), n)).decode())



if __name__ == "__main__":
    main()


```
