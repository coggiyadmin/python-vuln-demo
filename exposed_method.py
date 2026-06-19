"""CWE-749 — Exposed Dangerous Method or Function. A privileged maintenance routine is exposed
on an unauthenticated route. Real vuln; NO finding = FALSE NEGATIVE."""
import subprocess
from flask import Flask

app = Flask(__name__)


@app.route("/admin/maintenance")
def maintenance():
    # privileged maintenance action exposed with no auth gate → CWE-749
    return subprocess.check_output(["/opt/app/bin/cleanup.sh"]).decode()
