from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
def enc(key: bytes, data: bytes) -> bytes:
    iv = os.urandom(16)
    c = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    return iv + c.update(data) + c.finalize()
