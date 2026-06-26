import logging
import re
from flask import Flask, request
app = Flask(__name__)
log = logging.getLogger("app")
@app.route("/log")
def log_user():
    user = request.args.get("user", "")
    safe = re.sub(r"[\r\n\t]", "_", user)
    log.info("user=%s", safe)
    return "ok"
