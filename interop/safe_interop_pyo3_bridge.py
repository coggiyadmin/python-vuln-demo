"""Safe mirror — IL-68 PyO3 bridge caller."""
import shlex
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/pyo3")
def pyo3_bridge_safe():
    user = request.args.get("user", "")
    safe = shlex.quote(user)
    subprocess.run(["sh", "-c", f"echo {safe}"], check=False)
    return "ok"
