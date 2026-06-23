"""FN probe — CWE-434 unrestricted file upload: no extension/type validation (FN-19)."""
import os

from flask import Flask, request

app = Flask(__name__)
UPLOAD_DIR = "/var/www/uploads"


@app.route("/upload", methods=["POST"])
def upload():
    # SOURCE: attacker-controlled multipart filename + content
    f = request.files["file"]
    dest = os.path.join(UPLOAD_DIR, f.filename)
    # SINK (CWE-434): arbitrary filename/type persisted to a served dir → webshell
    f.save(dest)
    return "ok"
