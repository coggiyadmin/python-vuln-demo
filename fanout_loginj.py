"""Combination #11 — FAN-OUT × LOG INJECTION (CWE-117, Python)."""
import logging
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("combo")


@app.route("/fanout")
def fanout():
    u = request.args.get("u", "")  # SOURCE
    log.info("a " + u)  # sink 1
    log.warning("b " + u)  # sink 2
    log.error("c " + u)  # sink 3

