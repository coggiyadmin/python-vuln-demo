"""CWE-779 — Logging of Sensitive Data. The user's password is written to the application
log. Real vuln; NO finding = FALSE NEGATIVE. (CWE-532 family.)"""
import logging
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("app")


@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    pw = request.form["password"]          # SOURCE — credential
    log.info("login attempt user=%s password=%s", user, pw)   # logs the password → CWE-779
    return "ok"
