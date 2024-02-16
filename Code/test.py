
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import md5
from os import urandom
from Crypto.Util.number import *
from tqdm import *

last_block_flag = pad(b"}", 16)

enc_flag = 'ceb9223fccd91526c755cbb723086a63424a2565ab08d06857d043b4380b6611731bf80bf897284196e5310a9639797f68b56134a2ec1478ea496ba25473ea154ff694d6d5dd23e437a54e6613b06bdd'

enc_flag = bytes.fromhex(enc_flag)

last_block_enc = enc_flag[-16:]


for t in tqdm(range(2 ** 24)):

    key1 = t.to_bytes(3, byteorder = "little")
    
    key3 = key1
    key1 = md5(2*key1).digest()
    key3 = md5(2024*key3).digest()

    cipher1 = AES.new(key1, AES.MODE_ECB)
    cipher3 = AES.new(key3, AES.MODE_ECB)

    once = cipher1.encrypt(last_block_flag)
    third = cipher3.decrypt(last_block_enc)

    for x in range(256):
      
        key2 = md5(10*x.to_bytes(3, byteorder = "little")).digest()
        cipher2 = AES.new(key2, AES.MODE_ECB)

        if cipher2.decrypt(once) == third:
            flag =  cipher3.decrypt(enc_flag)
            flag = cipher2.encrypt(flag)
            flag = cipher1.decrypt(flag)

            print(f"This is flag: {flag}")
            exit()





