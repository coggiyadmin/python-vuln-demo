"""SAFE mirror — unsafe_reflection.py; resolve against a fixed allowlist registry,
never importing arbitrary modules. Expect 0 security findings."""
from flask import Flask, request

app = Flask(__name__)

REGISTRY = {"csv": lambda: "csv-export", "json": lambda: "json-export"}


@app.route("/make")
def make():
    name = request.args.get("fn", "")
    handler = REGISTRY.get(name)        # allowlist lookup — no reflection
    if handler is None:
        return "unknown", 400
    return str(handler())
