"""SAFE mirror — sensitive_info_exposure.py; the secret is written to a private, non-served
path with owner-only permissions. Expect 0 security findings."""
import os
from flask import Flask

app = Flask(__name__)


@app.route("/export-config")
def export_config():
    path = "/var/app/private/config.txt"   # not web-accessible
    fd = os.open(path, os.O_WRONLY | os.O_CREAT, 0o600)
    with os.fdopen(fd, "w") as f:
        f.write("API_KEY=" + os.environ.get("API_KEY", ""))
    return "exported"
