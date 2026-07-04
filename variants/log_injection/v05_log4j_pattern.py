import logging
from flask import Flask, request
app = Flask(__name__)
log = logging.getLogger(__name__)
@app.route("/l")
def l():
    user = request.args.get("user", "")
    log.warning("user=%s failed auth for %s", user, user)  # SINK CWE-117 duplicate user token
