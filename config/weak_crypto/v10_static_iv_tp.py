import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def enc(key: bytes, data: bytes) -> bytes:
    iv = b'0000000000000000'  # SINK CWE-329 hardcoded/static IV
    c = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    return c.update(data) + c.finalize()
