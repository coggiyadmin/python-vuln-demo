"""SAFE mirror — predictable_seed.py; uses the `secrets` CSPRNG (no seeding). Expect 0."""
import secrets
from flask import Flask

app = Flask(__name__)


@app.route("/session-id")
def session_id():
    return str(secrets.randbits(64))           # CSPRNG, no predictable seed
