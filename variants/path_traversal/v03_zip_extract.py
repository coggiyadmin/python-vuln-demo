import zipfile
from flask import Flask, request
app = Flask(__name__)
@app.route("/z")
def z():
    zf = request.files["f"]
    zipfile.ZipFile(zf).extractall("/tmp/out")  # SINK CWE-22 zip slip
