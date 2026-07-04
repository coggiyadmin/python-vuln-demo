"""IL-68 — Python PyO3 bridge caller (IL-3 FFI depth).

HTTP handler passes user input into a native-module-style subprocess spawn
(Python→Rust PyO3 boundary stand-in). Expected: FN at FFI edge until engine
models PyO3 re-exports.
"""
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/pyo3")
def pyo3_bridge():
    user = request.args.get("user", "")  # SOURCE
    subprocess.run(["sh", "-c", f"echo {user}"], check=False)  # SINK CWE-78 PyO3 boundary
    return "ok"
