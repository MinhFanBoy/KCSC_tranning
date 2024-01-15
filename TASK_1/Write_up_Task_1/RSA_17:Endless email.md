
### RSA_17

----

**_TASK:_**

Poor Johan has been answering emails all day and the students are all asking the same questions. Can you read his messages?

Challenge files:
  - johan.py
  - output.txt

----

Bài này sử dụng CRT vì tất cả các mũ e đểu bằng nhau.

```python


from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

txt = open("output.txt", "r").read().split("\n\n")

e = 3
lst = {}
t = 0

for i in txt:
    tmp = {}
    for x in i.split("\n"):
        if x != "":
            tmp[x.split(" = ")[0]] = int(x.split(" = ")[1])
    lst[t] = tmp
    t += 1

# n is modulus, a is remainder
def CRT(n: list, a: list) -> int:
    p = 1
    for i in n:
        p *= i
    sm = 0
    for i in range(len(n)):
        pp = p // n[i]
        sm += (a[i] * pow(pp, -1, n[i]) * pp) % p
    return sm % p

for x in range(7):
    for y in range(x + 1, 7):
        for z in range(y + 1, 7):
            n = [lst[x]["n"], lst[y]["n"], lst[z]["n"]]
            a = [lst[x]["c"], lst[y]["c"], lst[z]["c"]]

            c = CRT(n, a)

            m = long_to_bytes(iroot(c, e)[0])
            if b"crypto{" in m:
                print(m.decode())
                exit()

```
