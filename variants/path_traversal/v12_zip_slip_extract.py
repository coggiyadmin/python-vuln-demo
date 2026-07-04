import zipfile, io
from flask import Flask, request
app = Flask(__name__)
@app.route("/z", methods=["POST"])
def z():
    zipfile.ZipFile(io.BytesIO(request.get_data())).extractall("/var/www")  # SINK CWE-22 zip slip
