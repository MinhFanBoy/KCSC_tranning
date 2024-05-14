
Tables_of_content
----------------

### 1. Evil_ECB




```py
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
from os import urandom
import json
import socket
import threading

flag = 'KCSC{s0m3_r3ad4ble_5tr1ng_like_7his}'

menu = ('\n\n|---------------------------------------|\n' +
            '| Welcome to Evil_ECB!                  |\n' +
            '| Maybe we can change the Crypto world  |\n' +
            '| with a physical phenomena :D          |\n' +
            '|---------------------------------------|\n' +
            '| [1] Login                             |\n' +
            '| [2] Register ^__^                     |\n' +
            '| [3] Quit X__X                         |\n' +
            '|---------------------------------------|\n')

bye = ( '[+] Closing Connection ..\n'+
        '[+] Bye ..\n')

class Evil_ECB:
    def __init__(self):
        self.key = urandom(16)
        self.cipher = AES.new(self.key, AES.MODE_ECB)
        self.users = ['admin']

    def login(self, token):
        try:
            data = json.loads(unpad(self.cipher.decrypt(bytes.fromhex(token)), 16).decode())
            if data['username'] not in self.users:
                return '[-] Unknown user'

            if data['username'] == "admin" and data["isAdmin"]:
                return '[+] Hello admin , here is your secret : %s\n' % flag

            return "[+] Hello %s , you don't have any secret in our database" % data['username']
        except:
            return '[-] Invalid token !'
        
    def register(self, user):
        if user in self.users:
            return '[-] User already exists'
 
        data = b'{"username": "%s", "isAdmin": false}' % (user.encode())
        token = self.cipher.encrypt(pad(data, 16)).hex()
        self.users.append(user)
        return '[+] You can use this token to access your account : %s' % token

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        chal = Evil_ECB()
        client.send(menu.encode())
        for i in range(10):
            try:
                client.send(b'> ')
                choice = client.recv(size).strip()
                if choice == b'1':
                    client.send(b'Token: ')
                    token = client.recv(size).strip().decode()
                    client.send(chal.login(token).encode() + b'\n')
                elif choice == b'2':
                    client.send(b'Username: ')
                    user = client.recv(size).strip().decode()
                    client.send(chal.register(user).encode() + b'\n')
                elif choice == b'3':
                    client.send(bye.encode())
                    client.close()
                else:
                    client.send(b'Invalid choice!!!!\n')
                    client.close()
            except:
                client.close()
                return False
        client.send(b'No more rounds\n')
        client.close()

if __name__ == "__main__":
    ThreadedServer('',2003).listen()

```

Bài cho mình file server như này.

Tóm tắt lại file thì nó yêu cầu mình đăng nhập với tên là "admin" và isAdmin = "true" thì mình sẽ có flag (hàm login). Còn hàm register thì mình được đăng nhập với một tên tùy chọn và nó sẽ tạo ra một json có dạng như sau:

`{"username": "%s", "isAdmin": false}`

sau đó nó mã hóa json trên bằng AES.ECB mode để gửi tới server (Ngoài ra mình không được đăng ký tên user bằng admin).

Mình có mã hóa AES.ECB mode như sau:

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/2532b32e-c5d0-41af-8c30-53ab655430e3)

Mình thấy nó mẫ hóa các đầu vào thành các khối enc 16 bytes.

Mình thực hiện tấn công bằng cách gửi lại tên user name là chính cái json mình cần gửi cho hàm login là ta sẽ có nó được đoạn json mã hóa và thành công lấy được flag.

```py

from pwn import *
from json import *
from Crypto.Util.number import *
from Crypto.Util.Padding import pad, unpad

# nc 103.163.24.78 2003

s = remote("103.163.24.78", 2003)

print(s.recvuntil(b'> ').decode())
s.sendline(b"2")
print(s.recvuntil(b': ').decode())
s.sendline(b'bb' + pad(b'{"username": "admin"          , "isAdmin": true}', 16))

print(s.recvuntil(b': ').decode())


enc = bytes.fromhex(str(s.recvline()[:-1].decode()))[16: 48 + 32]

print(s.recvuntil(b'> ').decode())
s.sendline(b"1")
print(s.recvuntil(b': ').decode())
s.sendline(enc.hex())
print(s.recv().decode())


```

### 2. Micscrypt

```py

from PIL import Image
import numpy as np
import galois
GF256 = galois.GF(2**8)

img = Image.open('qr_flag_rgb.png')
pixels = img.load()
width, height = img.size

M = GF256(np.random.randint(0, 256, size=(3, 3), dtype=np.uint8))

# scan full height -> weight
for x in range(width):
    for y in range(0,height,3):
        A = GF256([pixels[x, y], pixels[x, y+1], pixels[x, y+2]])
        M = np.add(A, M)
        pixels[x, y], pixels[x, y+1], pixels[x, y+2] = [tuple([int(i) for i in j]) for j in M]

img.save('qr_flag_encrypt.png')
```

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/6c647279-da66-454d-96f3-22a4fb14d690)

Ta có một file và một ảnh. File chall là file mã hóa ảnh qr code thành ảnh qr code đã được mã hóa.

Ban đầu file sẽ tạo ra một ma trận M là một ma trận random trong trường GF($2 ^ 8$). Giả sử qr là một bẳng [a, b, c, ..] và qr được mã hóa là [a', b', c', ...]
thì ta có qr sẽ được mã hóa như sau:

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/1d4e8045-adfc-4b94-94d6-9b9e68fe312a)

Sau một lúc tìm hiểu thì mình thấy phần tử đầu tiên của một qr là màu đen, từ đó mình tìm được a. Dựa vào ảnh qr mã hóa mình có thể tìm lại M = a - a', từ đó mình có thể lật ngược các bước mã hóa để tìm lại qr ban đầu.

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/4fe9ad1f-6ee3-4bd0-a776-73229732fe3f)
