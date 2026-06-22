"""IL-1 polyglot — SAFE mirror of interop_shell_in_string.py.
No shell: the value is passed as a distinct argv element to a fixed program via
subprocess (no os.system string). The scanner MUST produce ZERO security findings.
"""
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")  # SOURCE
    # Safe: argv array, no shell — `host` is an operand to ping, never parsed as
    # shell syntax; "--" blocks option injection.
    subprocess.run(["ping", "-c", "1", "--", host])
    return "ok"
