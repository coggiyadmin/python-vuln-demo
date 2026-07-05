from Crypto.Cipher import DES
def enc(key: bytes, data: bytes) -> bytes:
    return DES.new(key, DES.MODE_ECB).encrypt(data)  # SINK CWE-327 DES weak cipher
