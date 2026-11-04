import subprocess
from flask import Flask, request
# cognium-dev#1072 — list-form subprocess keeps the sink when argv[0] is a shell
app = Flask(__name__)

@app.route("/run")
def run():
    cmd = request.args.get("c")
    subprocess.run(["sh", "-c", cmd])
    return "ok"
