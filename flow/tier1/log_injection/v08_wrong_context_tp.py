from html import escape
import logging
from flask import Flask, request
app = Flask(__name__)
log = logging.getLogger("app")
@app.route("/log")
def log_user():
    user = escape(request.args.get("user", ""))
    log.info("user=" + user)
    return "ok"
