"""SAFE mirror — unnecessary_privileges.py; drops to an unprivileged uid before the
operation. Expect 0 security findings."""
import os
import subprocess
from flask import Flask

app = Flask(__name__)
APP_UID = 1000


@app.route("/clearcache")
def clearcache():
    os.setuid(APP_UID)                        # drop privileges before acting
    subprocess.run(["rm", "-rf", "/var/app/cache"])
    return "ok"
