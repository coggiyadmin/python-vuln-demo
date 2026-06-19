"""CWE-426 — Untrusted Search Path. Invoking a binary by bare name with shell=True
relies on $PATH/cwd; an attacker-controlled PATH or cwd runs a malicious binary.
(Engine gap.) FN probe — NO finding = potential FALSE NEGATIVE."""
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/thumb")
def thumb():
    src = request.args.get("src", "")   # SOURCE (filename)
    # 'convert' resolved via $PATH; a planted ./convert or PATH entry runs → CWE-426
    subprocess.run("convert " + src + " out.png", shell=True)
    return "ok"
