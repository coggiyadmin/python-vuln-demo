import logging
from flask import Flask, request
app = Flask(__name__); log = logging.getLogger("app")
@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]; pw = request.form["password"]
    log.info("login user=%s password=%s", user, pw)  # SINK CWE-117
