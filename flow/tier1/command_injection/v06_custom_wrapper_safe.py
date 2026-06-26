import subprocess, shlex
from flask import Flask, request
def company_sanitize(x: str) -> str:
    return shlex.quote(x)
app = Flask(__name__)
@app.route("/c")
def c():
    q = company_sanitize(request.args.get("q", ""))
    subprocess.run(["grep", q, "/var/log/app.log"], shell=False)
