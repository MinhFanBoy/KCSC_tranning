
## RSA_2

---

**_Introduction:_**

Mã hóa RSA gồm có n = q * p với p, q là hai số nguyên tố và e (thường là 2 ^ 16 + 1). Một bộ khóa công khai gồm có (n, e)
Với m là bản rõ ta mã hóa như sau : c = pow(m, e, n)

**_Task:_**

Mã hóa m = 12, p = 17, q = 23, e = 65537

---

Theo công thức trên ta dễ có c = pow(m, e, q * p)

> 301
