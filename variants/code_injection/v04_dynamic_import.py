import importlib
from flask import Flask, request
app = Flask(__name__)
@app.route("/i")
def i():
    spec = request.args.get("spec", "")
    importlib.import_module(spec)  # SINK CWE-94
