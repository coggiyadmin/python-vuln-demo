import tarfile
from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def x():
    tarfile.open(request.args.get("path", "")).extractall("/var/data")  # SINK CWE-22 tar slip
