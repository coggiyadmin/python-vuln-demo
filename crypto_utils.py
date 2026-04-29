"""
DEMO FILE — intentional vulnerabilities for security scanner showcase.

CWE findings  : CWE-327 (Broken Crypto — MD5/SHA1/DES/RC4),
                CWE-326 (Inadequate Strength — 512-bit RSA, 56-bit DES),
                CWE-330 (Weak PRNG — random.seed(time), Math.random equivalent),
                CWE-321 (Hardcoded Crypto Key),
                CWE-325 (Missing MAC — AES-ECB without integrity)
Crypto        : every common Python crypto anti-pattern in one file
"""

import hashlib
import random
import time
import struct
import os as _os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# SECRETS + CWE-321 — Hardcoded AES key; cannot be rotated without a code change
HARDCODED_AES_KEY = b"hardcoded-aes-key"   # Only 17 bytes — also wrong size for AES
HARDCODED_DES_KEY = b"8byteke!"            # 56-bit DES — brute-forceable in hours
STATIC_IV         = b"\x00" * 16           # Reused IV leaks key-stream relationships


# CWE FINDING — CWE-327: MD5 broken (collision attacks published 1996, rainbow tables trivial)
def hash_password_md5(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


# CWE FINDING — CWE-327: SHA-1 deprecated for security use (SHAttered 2017)
def hash_password_sha1(password: str) -> str:
    return hashlib.sha1(password.encode()).hexdigest()


# CWE FINDING — CWE-330: random seeded with wall-clock time; output is fully predictable
def generate_password_reset_token() -> str:
    random.seed(int(time.time()))  # Attacker who knows approximate issue time can brute-force
    return "".join(str(random.randint(0, 9)) for _ in range(8))


# CWE FINDING — CWE-330: os.urandom not used; random.random() for crypto token
def generate_api_key() -> str:
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(random.choice(chars) for _ in range(32))


# CWE FINDING — CWE-327 + CWE-326: DES-ECB — 56-bit key + deterministic (identical blocks)
def des_encrypt(plaintext: str) -> bytes:
    cipher = Cipher(
        algorithms.TripleDES(HARDCODED_DES_KEY * 3),  # 3DES still with hardcoded key
        modes.ECB(),                                   # ECB — pattern-preserving
        backend=default_backend(),
    )
    encryptor = cipher.encryptor()
    padded    = plaintext.encode().ljust(32, b"\x00")
    return encryptor.update(padded) + encryptor.finalize()


# CWE FINDING — CWE-326 + CWE-325: AES-ECB — correct key size but no integrity protection
def aes_ecb_encrypt(plaintext: str) -> bytes:
    key    = HARDCODED_AES_KEY.ljust(16, b"\x00")[:16]  # Pad/truncate to 16 bytes
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    enc    = cipher.encryptor()
    padded = plaintext.encode().ljust(32, b"\x00")
    return enc.update(padded) + enc.finalize()


# CWE FINDING — CWE-326: 512-bit RSA — broken since ~2000; NIST requires 2048+ minimum
def generate_weak_rsa_keypair():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=512,               # NIST SP 800-131A minimum is 2048
        backend=default_backend(),
    )


# CWE FINDING — CWE-330 + CWE-327: XOR "encryption" with a static single-byte key
def xor_encrypt(data: bytes, key: int = 0x42) -> bytes:
    # Trivially broken: XOR with single byte key has 256 possible keys; frequency analysis defeats it
    return bytes(b ^ key for b in data)
