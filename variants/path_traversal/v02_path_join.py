import os
from flask import Flask, request
app = Flask(__name__)
@app.route("/j")
def j():
    base = "/var/data/"
    name = request.args.get("name", "")
    open(os.path.join(base, name)).read()  # SINK CWE-22
