
import socket
import threading
from Crypto.Cipher import AES
from os import urandom
import string


chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '_{}'
FLAG = b'KCSC{CBC_p4dd1ng_0racle_}'
assert all(i in chars for i in FLAG.decode())


def pad(msg, block_size):
    pad_len = 16 - len(msg) % block_size
    return msg + bytes([pad_len])*pad_len


def encrypt(key):
    iv = urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return (iv + cipher.encrypt(pad(FLAG,16)) ).hex().encode()
    
    
def decrypt(enc,key):
    enc = bytes.fromhex(enc)
    iv = enc[:16]
    ciphertext = enc[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    pad_len = decrypted[-1]
    if all(i == pad_len for i in decrypted[-pad_len:]):
        return b'Decrypted successfully.'
    else:
        return b'Incorrect padding.'
    
    
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
        while True:
            try:
                choice = client.recv(size).strip()
                if choice == b'encrypt':
                    client.send(encrypt(key) + b'\n')
                elif choice == b'decrypt':
                    client.send(b'Ciphertext: ')
                    c = client.recv(size).strip().decode()
                    client.send(decrypt(c,key) + b'\n')
            except:
                client.close()
                return False


if __name__ == "__main__":
    ThreadedServer('',2004).listen()
    