
## RSA_3

---

**_Introduction:_**

Trong RSA ta cần phải tính Phi(n) khi biết n. Đây là một bài toán khó khi n đủ lớn.

Giả sử: n = a^n * b^m * c^e ... (a, b, c là số nguyên tố)

=> phi(n) = n(1 - 1/a)(1 - 1/b)(1 - 1/c)

cũng tương tụ như thế với các n khác.

**_Task:_**

+ p = 857504083339712752489993810777
+ q = 1029224947942998075080348647219

tìm phi(n)

---

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

print((p - 1)*(q - 1))

> 882564595536224140639625987657529300394956519977044270821168
