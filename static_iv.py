"""CWE-1204 — Generation of Weak Initialization Vector. A static IV is used for AES-CBC,
so identical plaintexts encrypt identically. Real vuln; NO finding = FALSE NEGATIVE."""
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from flask import Flask, request

app = Flask(__name__)
KEY = b"0123456789abcdef0123456789abcdef"
IV = b"0000000000000000"                       # static IV → CWE-1204


@app.route("/enc")
def enc():
    c = Cipher(algorithms.AES(KEY), modes.CBC(IV)).encryptor()  # reused static IV → CWE-1204
    data = request.args.get("d", "").ljust(16).encode()
    return c.update(data) + c.finalize()
