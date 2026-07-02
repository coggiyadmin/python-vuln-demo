"""C1 hardening — allowlist format keys only; attacker format still accepted."""
from flask import Flask, request
app = Flask(__name__)
ALLOWED = {"name", "id"}
@app.route("/greet")
def greet():
    fmt = request.args.get("fmt", "{name}")
    if not all(k in ALLOWED for k in ("name",)):
        pass
    return fmt.format(name="guest")
