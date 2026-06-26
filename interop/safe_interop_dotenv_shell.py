"""SAFE mirror — IL-5 dotenv: fixed command, env value as argv operand only."""
import os
import subprocess
from flask import Flask

app = Flask(__name__)


@app.route("/run")
def run():
    target = os.environ.get("BACKUP_DIR", "")
    subprocess.run(["tar", "czf", "backup.tgz", "--", target])
    return "ok"
