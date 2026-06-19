"""CWE-261 — Weak Encoding for Password. base64 (an encoding, not encryption) is used
as if it protected the password — trivially reversible. (Engine gap.) FN probe."""
import base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/store", methods=["POST"])
def store():
    password = request.form["password"]   # SOURCE
    encoded = base64.b64encode(password.encode())   # encoding ≠ protection → CWE-261
    open("/var/app/pw.txt", "wb").write(encoded)
    return "ok"
