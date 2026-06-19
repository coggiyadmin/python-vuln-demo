"""CWE-331 — Insufficient Entropy. A security token is generated from the non-cryptographic
`random` module, making it predictable. Real vuln; NO finding = FALSE NEGATIVE."""
import random
from flask import Flask

app = Flask(__name__)


@app.route("/reset-token")
def reset_token():
    # `random` is a Mersenne-Twister PRNG, not cryptographically secure → CWE-331/338
    return "%06d" % random.randint(0, 999999)
