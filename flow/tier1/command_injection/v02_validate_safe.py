import subprocess
from flask import Flask, request, abort
app = Flask(__name__)
ALLOWED = {"daily", "weekly"}
@app.route("/c")
def c():
    q = request.args.get("q", "")
    if q not in ALLOWED: abort(403)
    subprocess.run(["grep", q, "/var/log/app.log"], shell=False)
