"""CVE-2024-3400 (PAN-OS GlobalProtect) — attacker session id becomes a shell/path component."""
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/ssl-vpn")
def handle():
    sessid = request.cookies.get("SESSID", "")           # SOURCE (attacker-controlled cookie)
    os.system("cat /var/appweb/sslvpndocs/" + sessid)    # SINK CWE-78 — path/command injection
    return "ok"
