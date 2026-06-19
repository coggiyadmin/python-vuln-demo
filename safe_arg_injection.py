"""SAFE mirror — arg_injection.py; `--` end-of-options separator prevents the value
from being parsed as a flag. Expect 0 security findings."""
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/log")
def gitlog():
    branch = request.args.get("branch", "")
    # `--` terminates option parsing; branch can no longer inject flags
    return subprocess.run(["git", "log", "--", branch], capture_output=True).stdout
