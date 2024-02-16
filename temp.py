
from pwn import *
from json import *


s = connect("localhost", 2004)

def encrypted():
    s.sendline(b"encrypt")
    return s.recv()

def decrypted(iv: bytes, enc: bytes) -> bytes:
    s.sendline(b"decrypt")
    s.sendline((iv + enc).hex().encode())
    if s.recv() == b'Decrypted successfully.':
        return True
    else: return False


tmp = bytes.fromhex(encrypted().decode())

iv = tmp[:16]
enc_flag = tmp[16:]


print(f"This is iv: {iv}")
print(f"This is enc_flag: {enc_flag}")

print(decrypted(iv, enc_flag))