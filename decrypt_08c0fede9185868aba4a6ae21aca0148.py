
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from pwn import *
from json import *
def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16)
    else:
        return plaintext
# socket.cryptohack.org 13373

s = remote("socket.cryptohack.org", 13373)

s.recv()

public_key = loads(s.recvline())

s.recvuntil(b":")

Bob_key_1 = loads(s.recvuntil(b"}"))

s.recvuntil(b":")

dict_1 = loads(s.recvuntil(b"}"))

s.recv()

tmp = {}

tmp["p"] = public_key["p"]

tmp["g"] = public_key["A"]
tmp["A"] = "0x01"
s.send(dumps(tmp).encode())

s.recvuntil(b":")

Bob_key_2 = loads(s.recvuntil(b"}"))
s.recvuntil(b":")

dict_2 = loads(s.recvuntil(b"}"))

shared_secret = int(Bob_key_2["B"], 16) % int(public_key["p"], 16)
iv = dict_1["iv"]
ciphertext = dict_1["encrypted"]

print(f"This is flag: {decrypt_flag(shared_secret, iv, ciphertext)}")

