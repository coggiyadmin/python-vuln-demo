"""CWE-335 — Incorrect Usage of Seeds in PRNG. The PRNG is seeded with the current time,
making its output predictable. Real vuln; NO finding = FALSE NEGATIVE."""
import random
import time
from flask import Flask

app = Flask(__name__)


@app.route("/session-id")
def session_id():
    random.seed(int(time.time()))              # predictable seed → CWE-335
    return str(random.getrandbits(64))
