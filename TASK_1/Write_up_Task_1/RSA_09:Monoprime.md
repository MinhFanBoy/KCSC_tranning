
## RSA_9

---
**_TASK_**

Why is everyone so obsessed with multiplying two primes for RSA. Why not just use one?

Challenge files:
  - [output.txt](https://cryptohack.org/static/challenges/output_086036e35349a406b94bfac9a7af6cca.txt)

---

```python


from Crypto.Util.number import *

def main():
    txt = open("output.txt", "r").read().split(" ")

    e = 65537
    n = int(txt[2])
    ct = int(txt[-3])

    print(long_to_bytes(pow(ct, pow(e, -1, n -1), n)).decode())

if __name__ == "__main__":
    main()


```
