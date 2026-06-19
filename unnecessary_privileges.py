"""CWE-250 — Execution with Unnecessary Privileges. The process escalates to root before
an operation that does not require it, instead of dropping privileges. (Engine gap.) FN probe."""
import os
import subprocess
from flask import Flask

app = Flask(__name__)


@app.route("/clearcache")
def clearcache():
    os.setuid(0)                              # escalate to root unnecessarily → CWE-250
    subprocess.run(["rm", "-rf", "/var/app/cache"])
    return "ok"
