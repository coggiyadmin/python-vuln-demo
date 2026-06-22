"""IL-1 polyglot — Python → shell DSL (CWE-78).

Host (Python) builds a guest-language (shell) snippet in a string from untrusted
input and runs it through the shell (`os.system`). Tests the shell-in-string sink.
"""
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")  # SOURCE (HTTP param)
    # SINK (CWE-78): shell guest-language command assembled in a Python string
    # and executed by the system shell.
    os.system("ping -c 1 " + host)
    return "ok"
