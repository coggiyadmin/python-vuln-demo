"""TP — OPatch-style unrestricted upload (CWE-434 intake pattern). CVE-2021-27860 class."""
import os

from flask import Flask, request

app = Flask(__name__)
UPLOAD_DIR = "/var/www/html/uploads"


@app.route("/opatch/upload", methods=["POST"])
def upload():
    f = request.files["patch"]
    dest = os.path.join(UPLOAD_DIR, f.filename)
    f.save(dest)  # SINK CWE-434
    return "ok"
