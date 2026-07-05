import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def enc(key: bytes, data: bytes) -> bytes:
    iv = os.urandom(16)  # random IV per message
    c = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    return iv + c.update(data) + c.finalize()
