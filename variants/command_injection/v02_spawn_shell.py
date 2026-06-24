import subprocess
from flask import Flask, request
app = Flask(__name__)
@app.route("/s")
def s():
    host = request.args.get("host", "")
    subprocess.call(["ping", "-c", "3", host], shell=True)  # SINK CWE-78
