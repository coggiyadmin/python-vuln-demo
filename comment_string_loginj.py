"""Combination #9 — COMMENT / STRING-LITERAL × LOG INJECTION (CWE-117, Python). Expect 0."""
import logging
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("combo")


@app.route("/x")
def x():
    u = request.args.get("user", "")
    # log.info("user " + u)  # commented
    example = "log.info(u)"
    return str(len(example) + len(u))

