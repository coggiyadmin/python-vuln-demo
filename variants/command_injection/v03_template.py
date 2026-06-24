import subprocess
from flask import Flask, request
app = Flask(__name__)
@app.route("/t")
def t():
    host = request.args.get("host", "")
    subprocess.check_output(f"ping -c 3 {host}", shell=True)  # SINK CWE-78
