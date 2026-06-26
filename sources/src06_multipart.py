from flask import Flask, request
import os
app = Flask(__name__)
@app.route("/up", methods=["POST"])
def h():
    f = request.files["f"]
    name = f.filename  # SOURCE SRC-06 multipart
    open(os.path.join("/tmp", name), "wb").write(f.read())  # SINK CWE-22
