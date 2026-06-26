"""c08 SAFE — custom wrapper × log injection (CWE-117). Expect clean."""
import logging
import re
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("app")


def redact(s):
    return re.sub(r"[\r\n\t]", "_", s)


@app.route("/wrapped")
def wrapped():
    log.info("user=%s", redact(request.args.get("user", "")))
