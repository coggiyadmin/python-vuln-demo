"""TP anchor (CWE-78) for #170 — a REAL OS command exec of untrusted HTTP input. Proves the engine
fires command_injection on a genuine OS sink, so safe_redis_protocol.py (a RESP protocol verb)
staying clean is a credited distinction, not an engine blind spot."""
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/run")
def run():
    cmd = request.args.get("cmd")  # attacker-controlled HTTP source
    return os.system(cmd)  # SINK — real OS command execution
