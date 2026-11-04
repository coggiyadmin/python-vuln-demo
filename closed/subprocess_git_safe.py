import subprocess
from flask import Flask, request
# cognium-dev#1072 — a non-shell program in argv[0] is not command injection
app = Flask(__name__)

@app.route("/run")
def run():
    cmd = request.args.get("c")
    subprocess.run(["git", "log", cmd])
    return "ok"
