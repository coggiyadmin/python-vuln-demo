"""Safe mirror — extension allowlist + secure_filename."""
import os

from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_DIR = "/var/data/patches"
ALLOWED = frozenset({".zip", ".jar", ".war"})


@app.route("/opatch/upload", methods=["POST"])
def upload():
    f = request.files["patch"]
    name = secure_filename(f.filename or "")
    ext = os.path.splitext(name)[1].lower()
    if not name or ext not in ALLOWED:
        return "unsupported", 400
    f.save(os.path.join(UPLOAD_DIR, name))
    return "ok"
