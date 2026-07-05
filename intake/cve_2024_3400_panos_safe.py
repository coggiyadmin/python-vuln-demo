"""SAFE — session id validated to a fixed shape and read via argv, no shell."""
import re
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/ssl-vpn")
def handle():
    sessid = request.cookies.get("SESSID", "")
    if not re.fullmatch(r"[A-Za-z0-9]{1,64}", sessid):
        return "bad", 400
    subprocess.run(["cat", "/var/appweb/sslvpndocs/" + sessid], shell=False)  # argv, validated
    return "ok"
