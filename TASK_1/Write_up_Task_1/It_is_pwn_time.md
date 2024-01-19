
### Crypto

---

**_TASK:_**
```py
from Crypto.Util.number import getPrime , bytes_to_long , GCD
import random
import time
import os
import json


random.seed(time.time())

flag = b'KCSC{T0o_much_t1mE_to_So1ve_T.T}' 

KEY_SIZE = 512
e = 65537
banner = 'RSA, or Rivest_Shamir_Adleman, is a widely-used public-key cryptosystem for secure communication. Can you break it ?'
print(banner)

def fast_exp(a, b, n):
    output = 1
    while b > 0:
        if b & 1:
            output = output * a % n
        a = a * a % n
        b >>= 1 
    return output    
def check(p, q, n):
    a_ = random.randint(1, 100)
    b_ = random.randint(1, 100)
    s = fast_exp(p, fast_exp(q, a_, (p - 1) * (q - 1)), n)
    t = fast_exp(q, fast_exp(p, b_, (p - 1) * (q - 1)), n)
    hint = s + t
    print(f'{hint = }')
def gen_RSA_params(N, e):
    p = getPrime(N)
    q = getPrime(N)
    while GCD(e, (p - 1) * (q - 1)) > 1:
        p = getPrime(N)
        q = getPrime(N)
    n = p * q
    check(p, q, n) 
    return (p, q, n)
p, q, n = gen_RSA_params(KEY_SIZE, e)

if __name__ == "__main__":
    print("Choose your option: ")
    print("1 : Get_Public_Key")
    print("2 : Get_ciphertext")
    print("3 : Check")
    while True:
     idx = json.loads(input())
     if idx['option'] == 'Get_Public_Key' :
      print(f'{n = }')
      print(f'{e = }')
     if idx['option'] == 'Get_ciphertext' :
      m = bytes_to_long(os.urandom(128))
      c = pow(m,e,n)
      print(f'ciphertext : {c}')
     if idx['option'] == 'check' :
      d = int(idx['private_key'],16)
      if pow(c,d,n) == m :
          print(f'Here is your flag : {flag}')
          break
      else :
          print('bruh')
```

---
