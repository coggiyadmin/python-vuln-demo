# SAFE — AES-GCM authenticated encryption.
from Crypto.Cipher import AES
import os
def enc(data: bytes) -> bytes:
    cipher = AES.new(os.urandom(16), AES.MODE_GCM)
    ct, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ct
