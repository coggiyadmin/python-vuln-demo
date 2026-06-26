import logging
from flask import Flask, request
def company_sanitize(x: str) -> str:
    return x.replace("\n", "")
app = Flask(__name__)
log = logging.getLogger("app")
@app.route("/log")
def log_user():
    log.info("user=" + company_sanitize(request.args.get("user", "")))
    return "ok"
