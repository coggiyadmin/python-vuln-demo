"""SAFE mirror — sensitive_data_logging.py; only non-sensitive fields are logged. Expect 0."""
import logging
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("app")


@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    request.form["password"]               # used for auth, never logged
    log.info("login attempt user=%s", user)   # no credential in the log
    return "ok"
