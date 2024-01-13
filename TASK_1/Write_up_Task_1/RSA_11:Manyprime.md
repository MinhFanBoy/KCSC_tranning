
## RSA_11

---

**_TASK_**

Using one prime factor was definitely a bad idea so I'll try using over 30 instead.

 If it's taking forever to factorise, read up on factorisation algorithms and make sure you're using one that's optimised for this scenario.


Challenge files:
  - [output.txt](https://cryptohack.org/static/challenges/output_5a478a5d4764257d0bbdfaed340fcbdd.txt)
    
---

```python


from gmpy2 import iroot
from Crypto.Util.number import *
from factordb.factordb import *

def main():
    txt = open("output.txt", "r").read().split("\n")

    n = int(txt[0][4:])
    e = 65537
    ct = int(txt[2][5:])
    
    primes = FactorDB(n)
    primes.connect()
    primes = primes.get_factor_list()

    phi = 1
    for x in primes:
        phi *= x - 1

    print(long_to_bytes(pow(ct, pow(e, -1, phi), n)).decode())

if __name__ == "__main__":
    main()


```
