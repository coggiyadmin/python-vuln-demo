import logging
from flask import Flask, request
app = Flask(__name__); log = logging.getLogger("app")
@app.route("/e")
def e():
    msg = request.args.get("msg", "")
    log.error("event: " + msg)  # SINK CWE-117 log forging
