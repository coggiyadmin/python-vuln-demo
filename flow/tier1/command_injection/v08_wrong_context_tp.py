from html import escape
import subprocess
from flask import Flask, request
app = Flask(__name__)
@app.route("/c")
def c():
    q = escape(request.args.get("q", ""))  # HTML escape — wrong for shell
    subprocess.call("grep " + q, shell=True)  # TP wrong context
