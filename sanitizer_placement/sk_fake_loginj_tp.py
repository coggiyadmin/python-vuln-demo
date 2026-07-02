"""C1 fake — strip newlines only before log sink."""
import logging
from flask import Flask, request
app = Flask(__name__); log = logging.getLogger("app")
@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("user", "").replace("\n", "")
    pw = request.form.get("password", "")
    log.info("login user=%s password=%s", user, pw)
