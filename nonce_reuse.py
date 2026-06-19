"""CWE-323 — Reusing a Nonce/Key Pair in Encryption. A fixed AES-GCM nonce is reused
across encryptions, breaking confidentiality/integrity. Real vuln; NO finding = FN."""
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from flask import Flask, request

app = Flask(__name__)
KEY = AESGCM.generate_key(bit_length=128)
NONCE = b"\x00" * 12                          # static nonce, reused → CWE-323


@app.route("/enc")
def enc():
    data = request.args.get("d", "").encode()
    return AESGCM(KEY).encrypt(NONCE, data, None)   # same NONCE every call → CWE-323
