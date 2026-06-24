# weak_crypto TP — AES-ECB (CWE-327).
from Crypto.Cipher import AES
KEY = b"0123456789abcdef"
def enc(data: bytes) -> bytes:
    return AES.new(KEY, AES.MODE_ECB).encrypt(data)  # SINK CWE-327
