"""SAFE mirror — static_iv.py; a fresh random IV is generated per encryption. Expect 0."""
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from flask import Flask, request

app = Flask(__name__)
KEY = b"0123456789abcdef0123456789abcdef"


@app.route("/enc")
def enc():
    iv = os.urandom(16)                        # unique IV per encryption
    c = Cipher(algorithms.AES(KEY), modes.CBC(iv)).encryptor()
    data = request.args.get("d", "").ljust(16).encode()
    return iv + c.update(data) + c.finalize()
