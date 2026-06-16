"""
PYTHON DEEP-DIVE — FALSE-NEGATIVE corpus (raises Python TPR/recall).

Every handler is a REAL vulnerability via a Python-specific sink that the
engine's config currently lacks or under-models. Any handler that produces NO
security finding is a FALSE NEGATIVE.
"""

import os
import pickle
import subprocess
import tarfile
import tempfile
import zipfile
from urllib.request import urlopen

from flask import Flask, request, send_from_directory
from sqlalchemy import create_engine, text

app = Flask(__name__)
engine = create_engine("postgresql://localhost/app")


# 1. SQLAlchemy text() — raw SQL injection (most common Python ORM raw path)
@app.route("/sa")
def sqlalchemy_raw():
    name = request.args.get("name", "")
    with engine.connect() as conn:
        # text() with f-string interpolation → SQL injection (CWE-89)
        return str(conn.execute(text(f"SELECT * FROM users WHERE name = '{name}'")).fetchall())


# 2. zipfile.extractall — Zip-Slip (CWE-22)
@app.route("/unzip", methods=["POST"])
def unzip():
    path = "/tmp/" + request.args.get("name", "u.zip")
    with zipfile.ZipFile(path) as zf:
        zf.extractall("/var/app/data")  # no entry-name validation → ../ escape
    return "ok"


# 3. tarfile.extractall — Tar-Slip (CWE-22)
@app.route("/untar", methods=["POST"])
def untar():
    path = request.args.get("path", "")
    with tarfile.open(path) as tf:
        tf.extractall("/var/app/data")  # CVE-2007-4559 class
    return "ok"


# 4. tempfile.mktemp — insecure predictable temp file (CWE-377)
@app.route("/tmpfile")
def tmpfile():
    name = request.args.get("name", "scratch")
    tmp = tempfile.mktemp(suffix=name)  # race condition / predictable path
    with open(tmp, "w") as fh:
        fh.write("data")
    return tmp


# 5. Flask send_from_directory — path traversal via filename
@app.route("/download")
def download():
    fname = request.args.get("f", "")
    return send_from_directory("/var/app/files", fname)  # ../ traversal


# 6. os.popen — command injection
@app.route("/lookup")
def lookup():
    domain = request.args.get("domain", "")
    return os.popen("whois " + domain).read()  # shell injection


# 7. subprocess shell=True with concatenation — command injection
@app.route("/scan")
def scan():
    target = request.args.get("target", "")
    out = subprocess.check_output("nmap " + target, shell=True)  # injection
    return out


# 8. pickle.load on request data — insecure deserialization (CWE-502)
@app.route("/restore", methods=["POST"])
def restore():
    return str(pickle.loads(request.get_data()))  # arbitrary object → RCE


# 9. urllib urlopen — SSRF
@app.route("/proxy")
def proxy():
    url = request.args.get("url", "")
    return urlopen(url).read()  # SSRF to internal / cloud metadata
