
## RSA_16

---

**_TASK_**

Okay so I got a bit carefree with my last script, but this time I've protected myself while keeping everything really big. Nothing will stop me and my supercomputer now!

Challenge files:
  - source.py
  - output.txt

---

c1:
```python


import owiener
from factordb.factordb import FactorDB
from gmpy2 import iroot
from Crypto.Util.number import *

def main():

    dict = {}
    txt = open("output.txt", "r").read().split("\n")

    
    for line in txt:
        tmp = line.split(" = ")
        dict[tmp[0]] = int(tmp[1], 16)

    primes = FactorDB(dict["N"])
    primes.connect()
    lst = primes.get_factor_list()

    phi = (lst[0] - 1) * (lst[1] - 1)

    print(long_to_bytes(pow(dict["c"], pow(dict["e"], -1, phi), dict["N"])).decode())


if __name__ == "__main__":
    main()



```


```python



```


