"""C1 hardening — basename strip only; traversal sequences remain."""
import os
from flask import Flask, request
app = Flask(__name__)
@app.route("/f")
def f():
    p = os.path.basename(request.args.get("p", ""))
    open("/data/" + p)
