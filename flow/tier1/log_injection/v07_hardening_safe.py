import logging
from flask import Flask, request, abort
app = Flask(__name__)
log = logging.getLogger("app")
@app.route("/log")
def log_user():
    user = request.args.get("user", "")
    if len(user) > 64:
        abort(400)
    log.info("user=%s", user)
    return "ok"
