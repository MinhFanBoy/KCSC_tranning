### Crypto_AES

----

**_TASK:_**

```python
import random
import time
import datetime  
import base64
from Crypto.Cipher import AES
flag = b"find_me"
iv = b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"

for i in range(0, 16-(len(flag) % 16)):
    flag += b"\0"

ts = time.time()

print("Flag Encrypted on %s" % datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M'))
seed = round(ts*1000)

random.seed(seed)

key = []
for i in range(0,16):
    key.append(random.randint(0,255))

key = bytearray(key)


cipher = AES.new(key, AES.MODE_CBC, iv) 
ciphertext = cipher.encrypt(flag)

enc = base64.b64encode(ciphertext).decode('utf-8')
print(enc)


# Flag Encrypted on 2023-08-02 10:27
# lQbbaZbwTCzzy73Q+0sRVViU27WrwvGoOzPv66lpqOWQLSXF9M8n24PE5y4K2T6Y

**_Hint:_**
+ Thời gian ở sever và máy tính có thể khác nhau
```

----

Bài này cx khá đơn giản, vì các số random không thật sự ngẫu nhiên mà nó chỉ lấy đầu vào là các số ngẫu nhiên rồi biến đổi nó nên cái mình cần là seed. Khi có seed rồi thì các số dược tạo nên key cũng sẽ hoàn toàn xác định và từ đó ta có thể có cờ.

Solution:
```py
import random
import time
import datetime  
import base64
from Crypto.Cipher import AES

for x in range(0, 24):
    date = "2023-08-02 "+ str(x) + ":27"
    tim = time.strptime(date,'%Y-%m-%d %H:%M')
    l = round(time.mktime(tim)*1000)

    flag = "lQbbaZbwTCzzy73Q+0sRVViU27WrwvGoOzPv66lpqOWQLSXF9M8n24PE5y4K2T6Y"
    flag = base64.b64decode(flag)
    print(flag)
    for i in range(l, l + 60000):

        random.seed(i)
        iv = b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"

        key = []
        for i in range(0,16):
            key.append(random.randint(0,255))

        key = bytearray(key)


        cipher = AES.new(key, AES.MODE_CBC, iv) 
        ciphertext = cipher.decrypt(flag)

        try:
            print(ciphertext.decode('utf-8'))
        except:
            pass

```
