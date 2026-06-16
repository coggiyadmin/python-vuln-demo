"""Combination #13 — ENCODED PAYLOADS (Python). Tainted input passes through a
decode step (base64 / URL-decode / bytes.decode) before the sink. Decoding does
NOT sanitize. Each is a REAL command injection; NO finding = FALSE NEGATIVE."""
import base64
import os
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)


# 13a. base64 decode then exec
@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    cmd = base64.b64decode(raw).decode()   # decode preserves taint
    os.system(cmd)                          # CWE-78


# 13b. URL-decode then exec
@app.route("/url")
def urld():
    raw = request.args.get("d", "")
    cmd = unquote(raw)                      # urllib unquote preserves taint
    os.system(cmd)                          # CWE-78


# 13c. bytes → str decode then exec
@app.route("/bytes")
def b():
    raw = request.args.get("d", "")
    cmd = raw.encode("utf-8").decode("utf-8")  # round-trip, still tainted
    os.system("echo " + cmd)                    # CWE-78
