"""SAFE mirror — nonce_reuse.py; a fresh random nonce is generated per encryption. Expect 0."""
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from flask import Flask, request

app = Flask(__name__)
KEY = AESGCM.generate_key(bit_length=128)


@app.route("/enc")
def enc():
    nonce = os.urandom(12)                     # unique nonce per encryption
    data = request.args.get("d", "").encode()
    return nonce + AESGCM(KEY).encrypt(nonce, data, None)
