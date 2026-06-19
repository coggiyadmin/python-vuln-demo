"""SAFE mirror — exposed_method.py; the privileged action requires an authenticated admin."""
import os
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/admin/maintenance")
def maintenance():
    if request.headers.get("X-Admin-Token") != os.environ.get("ADMIN_TOKEN"):  # auth gate
        return "forbidden", 403
    return subprocess.check_output(["/opt/app/bin/cleanup.sh"]).decode()
