### Crypto

---

**_TASK:_**

Been cooking up my own padding scheme, now my encrypted flag is different everytime!

*Connect at socket.cryptohack.org 13386*

Challenge files:
  - 13386.py

---

Ở bài này, ta có cách pad là thêm với hệ số a, b. Có:
$$(a_1 * m + b_1) ^ {e} = c_1 \pmod{n} \quad \to \quad p_1 \equiv (a_1 * m + b_1) ^ {e} - c_1 \equiv 0 \pmod{n}$$
$$(a_2 * m + b_2) ^ {e} = c_2 \pmod{n} \quad \to \quad p_2 \equiv (a_2 * m + b_2) ^ {e} - c_2 \equiv 0 \pmod{n}$$

Vì cả hai hệ có chung một nghiệm là $m$ nên khi lấy $GCD(p_1, p_2)$ thì ta sẽ có được m. Để lấy được gcd của đa thức ta có thể sử dụng Euclidean algorithm.
$$a * p_1 + b * p_2 = gcd(p_1, p_2) \quad \forall a, b \in R$$

ở 
