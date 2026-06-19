"""CWE-257 — Storing Passwords in a Recoverable Format. The password is reversibly
encrypted (symmetric, key on hand) so it can be decrypted back to cleartext. (Engine
gap.) FN probe — NO finding = potential FALSE NEGATIVE."""
from cryptography.fernet import Fernet
from flask import Flask, request

app = Flask(__name__)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)


@app.route("/store", methods=["POST"])
def store():
    password = request.form["password"]   # SOURCE
    token = cipher.encrypt(password.encode())   # reversible — recoverable to cleartext → CWE-257
    open("/var/app/pw.bin", "wb").write(token)
    return "ok"
