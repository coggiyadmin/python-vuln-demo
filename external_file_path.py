"""CWE-73 — External Control of File Name or Path. User fully controls the path
passed to open() — absolute paths and traversal both reachable. NO finding = FN."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/read")
def read():
    path = request.args.get("path", "")   # SOURCE — full path, attacker-controlled
    return open(path).read()               # arbitrary file read (e.g. /etc/passwd) → CWE-73
