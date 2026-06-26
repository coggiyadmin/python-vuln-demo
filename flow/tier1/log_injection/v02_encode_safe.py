# Phase-3 encode mirror
import logging
from flask import Flask, request
app = Flask(__name__); log = logging.getLogger("app")
@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    log.info("login user=%s", user)  # SAFE — no password in log
