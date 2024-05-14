
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

### 3. square

```py

from os import urandom
from aes import AES
import socket
import threading

flag = 'KCSC{s0m3_r3ad4ble_5tr1ng_like_7his}'

menu = ('\n\n|---------------------------------------|\n' +
            '| Welcome to KCSC Square!               |\n' +
            '| I know it\'s late now but              |\n' +
            '| Happy Reunification Day :D            |\n' +
            '|---------------------------------------|\n' +
            '| [1] Get ciphertext                    |\n' +
            '| [2] Guess key ^__^                    |\n' +
            '| [3] Quit X__X                         |\n' +
            '|---------------------------------------|\n')

bye = ( '[+] Closing Connection ..\n'+
        '[+] Bye ..\n')

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
        key = urandom(16)
        chal = AES(key)
        client.send(menu.encode())
        for i in range(8888):
            try:
                client.send(b'> ')
                choice = client.recv(size).strip()
                if choice == b'1':
                    client.send(b'Plaintext in hex: ')
                    hex_pt = client.recv(size).strip().decode()
                    try:
                        pt = bytes.fromhex(hex_pt)
                        assert len(pt) == 16
                    except:
                        client.send(b'Something wrong in your plaintext' + b'\n')
                        continue
                    client.send(chal.encrypt(pt).hex().encode() + b'\n')
                elif choice == b'2':
                    client.send(b'Key in hex: ')
                    hex_key = client.recv(size).strip().decode()
                    try:
                        guess_key = bytes.fromhex(hex_key)
                        assert guess_key == key
                    except:
                        client.send(b'Wrong key, good luck next time =)))' + b'\n')
                        client.close()
                    client.send(b'Nice try, you got it :D!!!! Here is your flag: ' + flag.encode() + b'\n')
                    client.close()
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
    ThreadedServer('',2004).listen()
```

```py

class AES:
    sbox = (
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
    )

    rcon = (0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36)

    gmul2 = (
        0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e, 
        0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e, 
        0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e, 
        0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e, 
        0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e, 
        0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe, 
        0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde, 
        0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe, 
        0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05, 
        0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25, 
        0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45, 
        0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65, 
        0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85, 
        0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5, 
        0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5, 
        0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5
    )

    gmul3 = (
        0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11, 
        0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21, 
        0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71, 
        0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41, 
        0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1, 
        0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1, 
        0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1, 
        0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81, 
        0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a, 
        0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba, 
        0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea, 
        0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda, 
        0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a, 
        0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a, 
        0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a, 
        0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a
    )

    def __init__(self, key):
        self._block_size = 16
        self._round_keys = self._expand_key([i for i in key])
        self._state = []

    def _transpose(self, m):
        return [m[4 * j + i] for i in range(4) for j in range(4)]

    def _xor(self, a, b):
        return [x ^ y for x, y in zip(a, b)]

    def _expand_key(self, key):
        round_keys = [key]

        for i in range(4):
            round_key = []
            first = round_keys[i][:4]
            last = round_keys[i][-4:]
            last = last[1:] + [last[0]]
            last = [self.sbox[i] for i in last]

            round_key.extend(self._xor(self._xor(first, last), [self.rcon[i+1], 0, 0, 0]))
            for j in range(0, 12, 4):
                round_key.extend(self._xor(round_key[j:j + 4], round_keys[i][j + 4:j + 8]))
            round_keys.append(round_key)

        for i in range(len(round_keys)):
            round_keys[i] = self._transpose(round_keys[i])

        return round_keys

    def _add_round_key(self, i):
        self._state = self._xor(self._round_keys[i], self._state)

    def _mix_columns(self):
        s = [0] * self._block_size
        for i in range(4):
            s[i] = self.gmul2[self._state[i]] ^ self.gmul3[self._state[i + 4]] ^ self._state[i + 8] ^ self._state[i + 12]
            s[i + 4] = self._state[i] ^ self.gmul2[self._state[i + 4]] ^ self.gmul3[self._state[i + 8]] ^ self._state[i + 12]
            s[i + 8] = self._state[i] ^ self._state[i + 4] ^ self.gmul2[self._state[i + 8]] ^ self.gmul3[self._state[i + 12]]
            s[i + 12] = self.gmul3[self._state[i]] ^ self._state[i + 4] ^ self._state[i + 8] ^ self.gmul2[self._state[i + 12]]
        self._state = s

    def _shift_rows(self):
        self._state = [
            self._state[0], self._state[1], self._state[2], self._state[3],
            self._state[5], self._state[6], self._state[7], self._state[4],
            self._state[10], self._state[11], self._state[8], self._state[9],
            self._state[15], self._state[12], self._state[13], self._state[14]
        ]

    def _sub_bytes(self):
        self._state = [self.sbox[i] for i in self._state]

    def _encrypt_block(self):
        self._add_round_key(0)

        for i in range(1, 4):
            self._sub_bytes()
            self._shift_rows()
            self._mix_columns()
            self._add_round_key(i)

        self._sub_bytes()
        self._shift_rows()
        self._add_round_key(4)

    def encrypt(self, plaintext):
        ciphertext = b''

        self._state = self._transpose([c for c in plaintext])
        self._encrypt_block()
        ciphertext += bytes(self._transpose(self._state))

        return ciphertext
```

Bài này là bài mã hóa AES, server cho mình gửi plaintext trả lại cho mình enc và yêu cầu tìm lại key. Tuy nhiên AES này đã được custom lại nhưng

```
    def _encrypt_block(self):
        self._add_round_key(0)

        for i in range(1, 4):
            self._sub_bytes()
            self._shift_rows()
            self._mix_columns()
            self._add_round_key(i)

        self._sub_bytes()
        self._shift_rows()
        self._add_round_key(4)
```

Mỗi hàm enc_block bị giảm lại số vòng mã hóa điều này khiến cho AES bị phá vỡ.

Giả sử trong một tập hợp 16 bytes plaintext thì với một vị trí thay đổi thì ta có sẽ có các enc khác nhau. Giả sử bytes thay đổi có vị trí là 1, sau 4 vòng AES thì ta sẽ có các vị trí bị thay đổi như sau( hiệu ứng tuyết lở)

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/345d1a82-ae8a-48ca-b0c7-bda82f587720)

giait thích qua về các vòng:

+ add_round_key: vì đây là phép xor nên sau khi thực hiện dòng này thì vị trí bị thay đổi vẫn là những vị trí cũ
+ subbytes: vì trong mỗi một s_box chỉ có một giá trị s_box[i] với mỗi i duy nhất nên ta thấy vị trí bị thay đổi vẫn như cũ
+ shift_row: hàm này đổi chỗ phần tử của các hàm tuy vị trí có bị thay đổi nhưng số vị trí bị ảnh hưởng vẫn không thay đổi so với ban đầu
+ mix_collums: hàm này là hàm nhân ma trận nên vị trí hoạt động có bị thay đổi ở những chỗ nhân với các phần tử bị thay thế


![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/e9b262c9-1518-406f-92b6-777c87f07c34)

Từ sau lần mã hóa thứ 3 tất cả các bytes đã bị thay đổi. Nhưng ta có thu được tính chất như sau:


![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/aa4e5a8d-f161-449e-88c9-d2eaa59253de)

Tính chất này áp dụng với mọi vị trí của plaintext.

Tại round thứ 4 ta sẽ làm như sau:

+ gọi ví trí bị thay đổi là i, ta đoán round_key[4][i] = guess. Từ đó ciphertext[i] = ciphertext[i] ^ roundKey[i]
+ sau đó ta thực hiện hàm InvShiftRows và InvSubBytes với ciphertext. Nếu ciphertext thỏa mãn tính chất trên thì guess có thể là giá trị ta đang cần tìm. Ta chỉ cần thử đến khi chỉ còn 1 giá trị guess thỏa mãn và tìm lại được hết round_key[4]
+ sau đó từ round_key tại 4 ta có thể tìm lại được key bằng hàm có sẵn của python

```py


from pwn import *
from tqdm import *
import os
from aes import *
from aeskeyschedule import reverse_key_schedule

# nc 103.163.24.78 2004

InvS_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)
target = connect("103.163.24.78", 2004)

def encrypt(pt:bytes):

    target.sendlineafter(b"> ", b"1")
    target.sendlineafter(b"Plaintext in hex: ", pt.hex().encode())
    ct = target.recvline()[:-1].decode()
    return bytes.fromhex(ct)

def find_key_bytes(idx:int):

    real_ans = set(list(range(256)))
    key_pos = [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]

    while True:
        ans = set()
        A_set = []
        init = os.urandom(16)
        for i in range(256):
            temp = bytearray(init)
            temp[idx] = i
            A_set += [encrypt(temp)]
        
        for i in range(256):
            A_set_dec = 0
            for ele in A_set:

                A_set_dec ^= InvS_box[ele[idx] ^ i]

            if A_set_dec == 0:
                ans.add(i)

        real_ans.intersection_update(ans)

        if len(real_ans) == 1:
            return real_ans.pop()

key = []
for i in tqdm(range(16)):
    ans = find_key_bytes(i)
    key.append(ans)

hexkey = reverse_key_schedule(bytes(key), 4).hex()

print(hexkey)

target.sendlineafter(b"> ", b"2")
target.sendlineafter(b'Key in hex: ', hexkey.encode())
print(target.recv())

```

Nguồn:

+ [https://hackmd.io/@Giapppp/square_attack#AES-3-round]
+ [https://www.davidwong.fr/blockbreakers/square_1_3rounds.html]

### 4. don_copper

```py
import random
from Crypto.Util.number import getPrime

NBITS = 2048

def pad(msg, nbits):
    """msg -> trash | 0x00 | msg"""
    pad_length = nbits - len(msg) * 8 - 8
    assert pad_length >= 0
    pad = random.getrandbits(pad_length).to_bytes((pad_length+7) // 8, "big")
    return pad + b"\x00" + msg


if __name__ == '__main__':
    p = getPrime(NBITS//2)
    q = getPrime(NBITS//2)
    n = p*q
    e = 3
    print('n =',n)

    flag = b'KCSC{s0m3_r3ad4ble_5tr1ng_like_7his}'
    flag1 = int.from_bytes(pad(flag[:len(flag)//2], NBITS-1), "big")
    flag2 = int.from_bytes(pad(flag[len(flag)//2:], NBITS-1), "big")
    print('c1 =', pow(flag1, e, n))
    print('c2 =', pow(flag2, e, n))
    print('c3 =', pow(flag1 + flag2 + 2024, e, n))

'''
n = 20309506650796881616529290664036466538489386425747108847329314416833872927305399144955238770343216928093685748677981345624111315501596571108286475815937548732237777944966756121878930547704154830118623697713050651175872498696886388591990290649008566165706882183536432074074093989165129982027471595363186012032012716786766898967178702932387828604019583820419525077836905310644900660107030935400863436580408288191459013552406498847690908648207805504191001496170310089546275003489343333654260825796730484675948772646479183783762309135891162431343426271855443311093315537542013161936068129247159333498199039105461683433559
c1 = 4199114785395079527708590502284487952499260901806619182047635882351235136067066118088238258758190817298694050837954512048540738666568371021705303034447643372079128117357999230662297600296143681452520944664127802819585723070008246552551484638691165362269408201085933941408723024036595945680925114050652110889316381605080307039620210609769392683351575676103028568766527469370715488668422245141709925930432410059952738674832588223109550486203200795541531631718435391186500053512941594901330786938768706895275374971646539833090714455557224571309211063383843267282547373014559640119269509932424300539909699047417886111314
c2 = 15650490923019220133875152059331365766693239517506051173267598885807661657182838682038088755247179213968582991397981250801642560325035309774037501160195325905859961337459025909689911567332523970782429751122939747242844779503873324022826268274173388947508160966345513047092282464148309981988907583482129247720207815093850363800732109933366825533141246927329087602528196453603292618745790632581329788674987853984153555891779927769670258476202605061744673053413682672209298008811597719866629672869500235237620887158099637238077835474668017416820127072548341550712637174520271022708396652014740738238378199870687994311904
c3 = 18049611726836505821453817372562316794589656109517250054347456683556431747564647553880528986894363034117226538032533356275073007558690442144224643000621847811625558231542435955117636426010023056741993285381967997664265021610409564351046101786654952679193571324445192716616759002730952101112316495837569266130959699342032640740375761374993415050076510886515944123594545916167183939520495851349542048972495703489407916038504032996901940696359461636008398991990191156647394833667609213829253486672716593224216112049920602489681252392770813768169755622341704890099918147629758209742872521177691286126574993863763318087398
'''

```

Tóm tắt lại đề bài mình thấy, FLag được chia ra làm hai phần theo dạng như sau:

            """msg -> trash | 0x00 | msg"""

Và ta có các thông tin như sau:

- $$f_1 ^ {3} = c1$$
- $$f_2 ^ {3} = c2$$
- $$(f_1 + f_2 + 2024) ^ {3} = c3$$

Bài này mình hiện tại thấy có hai hướng như sau:

#### Hướng 1:

Chuyển vế cả hai phương trình ta có:

- $$f_1 ^ {3} - c1 = 0 (mod n)$$
- $$f_2 ^ {3} - c2 = 0 (mod n)$$
- $$(f_1 + f_2 + 2024) ^ {3} - c3 = 0 (mod n)$$

Với resultant của một đa thức được tính như sau:

![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/dd6307dd-a3f9-4871-bc63-09203f6ed1ae)

Giả sử có một hệ gồm hai phương trình đại số với các hệ số từ trường P như sau:

+ f(x, y) = 0
+ g(x, y) = 0

và mỗi phương trình có thể viết lại như sau:

+ $f(x,y) = a_0 * (y) * x_k + a_1 * (y) * x_{k−1} + ⋯ + a_k * (y)$
+ $g(x,y) = b_0 * (y) * x_l + b_1 * (y) * x_{l−1} + ⋯ + b_l * (y)$

Coi y là một tham số ta có Re(f, g) = F(y) từ đó nó trở thành hàm một biến. Với một số z thỏa mãn F(z) = 0 thì ta luôn có GCD(f(x, z), g(z, z)) != 0

Áp dụng vào trường hợp bài này, mình tính Re(f_1, _3) và Re(f_2, f_3) từ đó GCD(f(y), f'(y)) = flag_2. Sau khi có flag 2 mình sử dụng GCD(f_1, f_3) = flag_1

```py
from Crypto.Util.number import *

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a, b

def poly_gcd(a,b) :

    while b :
        a , b = b , a%b 
    return a.monic()

n = 20309506650796881616529290664036466538489386425747108847329314416833872927305399144955238770343216928093685748677981345624111315501596571108286475815937548732237777944966756121878930547704154830118623697713050651175872498696886388591990290649008566165706882183536432074074093989165129982027471595363186012032012716786766898967178702932387828604019583820419525077836905310644900660107030935400863436580408288191459013552406498847690908648207805504191001496170310089546275003489343333654260825796730484675948772646479183783762309135891162431343426271855443311093315537542013161936068129247159333498199039105461683433559
c1 = 4199114785395079527708590502284487952499260901806619182047635882351235136067066118088238258758190817298694050837954512048540738666568371021705303034447643372079128117357999230662297600296143681452520944664127802819585723070008246552551484638691165362269408201085933941408723024036595945680925114050652110889316381605080307039620210609769392683351575676103028568766527469370715488668422245141709925930432410059952738674832588223109550486203200795541531631718435391186500053512941594901330786938768706895275374971646539833090714455557224571309211063383843267282547373014559640119269509932424300539909699047417886111314
c2 = 15650490923019220133875152059331365766693239517506051173267598885807661657182838682038088755247179213968582991397981250801642560325035309774037501160195325905859961337459025909689911567332523970782429751122939747242844779503873324022826268274173388947508160966345513047092282464148309981988907583482129247720207815093850363800732109933366825533141246927329087602528196453603292618745790632581329788674987853984153555891779927769670258476202605061744673053413682672209298008811597719866629672869500235237620887158099637238077835474668017416820127072548341550712637174520271022708396652014740738238378199870687994311904
c3 = 18049611726836505821453817372562316794589656109517250054347456683556431747564647553880528986894363034117226538032533356275073007558690442144224643000621847811625558231542435955117636426010023056741993285381967997664265021610409564351046101786654952679193571324445192716616759002730952101112316495837569266130959699342032640740375761374993415050076510886515944123594545916167183939520495851349542048972495703489407916038504032996901940696359461636008398991990191156647394833667609213829253486672716593224216112049920602489681252392770813768169755622341704890099918147629758209742872521177691286126574993863763318087398
P.<x, y> = PolynomialRing(ZZ, 2)
f1 = x ^ 3 - c1
f2 = y ^ 3 - c2
f3 = (x + y + 2024) ^ 3 - c3

a = f3.resultant(f1)
b = f3.resultant(f2)

k_1 = a.change_ring(Zmod(n))
k_2 = b.change_ring(Zmod(n))
print(gcd(k_1, k_2)[0])

flag2 = 9459443586581095463222963515045541750050401827723510705897500844799849261796406122135832441811940892678449284915507438180096529581822225557897730433367197311003395728481898399515202115480579351214154911161912655602477194436184856558515835058015571619614345184856562451617679600835568387776441880108026575993352354489949517485766579574832509082847320808015006029124439688311872585337604535334424350911596931057233568004228280191818255292666659478504955303928953745445941906638012999599402752288535775898414246173357868989327697475521090706257373290980287687716002708347360632676822894654445041725867378041786245727357
   
P.<x> = PolynomialRing(Zmod(n))
f1 = (x)^3 - c1
f2 = (x+ flag2 + 2024)^3 - c3

print(-poly_gcd(f1,f2)[0] % n)

# KCSC{W0rk1ng_w1th_p0lyn0m14ls_1s_34sy_:D}
```

#### Hướng 2

Mình là theo các của anh Quốc như sau:

Đưu nó về ideal trong Zmod(n) sau đó đưa nó về groebner_basis để tìm lại ideal nhỏ nhất ứng với các phần tử thỏa mãn là flag_1 và flag_2. Maybe ?!

```py
n = 20309506650796881616529290664036466538489386425747108847329314416833872927305399144955238770343216928093685748677981345624111315501596571108286475815937548732237777944966756121878930547704154830118623697713050651175872498696886388591990290649008566165706882183536432074074093989165129982027471595363186012032012716786766898967178702932387828604019583820419525077836905310644900660107030935400863436580408288191459013552406498847690908648207805504191001496170310089546275003489343333654260825796730484675948772646479183783762309135891162431343426271855443311093315537542013161936068129247159333498199039105461683433559
c1 = 4199114785395079527708590502284487952499260901806619182047635882351235136067066118088238258758190817298694050837954512048540738666568371021705303034447643372079128117357999230662297600296143681452520944664127802819585723070008246552551484638691165362269408201085933941408723024036595945680925114050652110889316381605080307039620210609769392683351575676103028568766527469370715488668422245141709925930432410059952738674832588223109550486203200795541531631718435391186500053512941594901330786938768706895275374971646539833090714455557224571309211063383843267282547373014559640119269509932424300539909699047417886111314
c2 = 15650490923019220133875152059331365766693239517506051173267598885807661657182838682038088755247179213968582991397981250801642560325035309774037501160195325905859961337459025909689911567332523970782429751122939747242844779503873324022826268274173388947508160966345513047092282464148309981988907583482129247720207815093850363800732109933366825533141246927329087602528196453603292618745790632581329788674987853984153555891779927769670258476202605061744673053413682672209298008811597719866629672869500235237620887158099637238077835474668017416820127072548341550712637174520271022708396652014740738238378199870687994311904
c3 = 18049611726836505821453817372562316794589656109517250054347456683556431747564647553880528986894363034117226538032533356275073007558690442144224643000621847811625558231542435955117636426010023056741993285381967997664265021610409564351046101786654952679193571324445192716616759002730952101112316495837569266130959699342032640740375761374993415050076510886515944123594545916167183939520495851349542048972495703489407916038504032996901940696359461636008398991990191156647394833667609213829253486672716593224216112049920602489681252392770813768169755622341704890099918147629758209742872521177691286126574993863763318087398
P.<x,y> = PolynomialRing(Zmod(n))
f1 = (x)^3 - c1
f2 = (y)^3 - c2
f3 = (x + y + 2024)^3 - c3

I = P.ideal(f1,f2,f3)

for eq in I.groebner_basis():
    print(eq)
```
