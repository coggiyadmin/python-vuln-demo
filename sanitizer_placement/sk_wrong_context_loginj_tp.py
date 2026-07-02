"""C1 wrong-context — HTML escape before log sink."""
import html
import logging
from flask import Flask, request
app = Flask(__name__); log = logging.getLogger("app")
@app.route("/login", methods=["POST"])
def login():
    user = html.escape(request.form.get("user", ""))
    pw = request.form.get("password", "")
    log.info("login user=%s password=%s", user, pw)
