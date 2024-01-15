
### RSA_18

---

**_TASK:_**

Finding large primes is slow, so I've devised an optimisation.

Challenge files:
  - descent.py
  - output.txt

---

```python


from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot

def main():
    
    txt = open('output.txt', 'r').read().split('\n')
    dict = {}
    for i in txt:
        if i != '':
            dict[i.split(' = ')[0]] = int(i.split(' = ')[1])
    
    def Fermat_attack(n):
        a = iroot(n, 2)[0] + 1
        b = iroot(a * a - n, 2)[0]
        while n != a**2 - b**2:
            a += 1
            b = a * a - n

        return (a+b, a-b)
    
    p, q = Fermat_attack(dict['n'])
    print(f"p = {p}")
    print(f"q = {q}")

    phi = (p-1) * (q-1)
    d = pow(dict['e'], -1, phi)
    print(long_to_bytes(pow(dict['c'], d, dict['n'])).decode())


if __name__ == '__main__':
    main()



```

