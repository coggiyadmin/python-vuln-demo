import subprocess
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/c")
def c():
    q = request.args.get("q", "")
    if any(c in q for c in ";|&$`"):
        abort(400)
    subprocess.run(["grep", q, "/var/log/app.log"], shell=False)
