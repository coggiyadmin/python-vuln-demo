import subprocess
from flask import Flask, request
app = Flask(__name__)
@app.route("/c")
def c():
    q = request.args.get("q", "")
    subprocess.run(["grep", q, "/var/log/app.log"], shell=False)  # framework argv API
