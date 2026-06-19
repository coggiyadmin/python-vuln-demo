"""CWE-88 — Argument Injection. User input passed as a CLI argument without a `--`
separator can inject extra flags. Real vuln; NO finding = FALSE NEGATIVE."""
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/log")
def gitlog():
    branch = request.args.get("branch", "")   # SOURCE
    # branch like "--output=/etc/cron.d/x" is parsed as an OPTION, not a value → CWE-88
    return subprocess.run(["git", "log", branch], capture_output=True).stdout
