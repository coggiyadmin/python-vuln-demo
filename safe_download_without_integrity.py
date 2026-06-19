"""SAFE mirror — download_without_integrity.py; verifies a pinned SHA-256 over HTTPS before
executing. Expect 0 security findings."""
import hashlib
import subprocess
import requests
from flask import Flask

app = Flask(__name__)
EXPECTED_SHA256 = "9f2c...pinned...digest"


@app.route("/self-update")
def self_update():
    code = requests.get("https://updates.internal/install.sh", verify=True).text
    if hashlib.sha256(code.encode()).hexdigest() != EXPECTED_SHA256:  # integrity check
        return "integrity check failed", 400
    subprocess.run(["bash", "-c", code])
    return "updated"
