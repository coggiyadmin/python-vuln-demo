"""SAFE mirror — insufficient_entropy.py; uses the `secrets` CSPRNG. Expect 0 findings."""
import secrets
from flask import Flask

app = Flask(__name__)


@app.route("/reset-token")
def reset_token():
    return secrets.token_hex(16)               # cryptographically secure
