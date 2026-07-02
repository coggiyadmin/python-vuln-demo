"""C1 fake — comment-only before format string."""
from flask import Flask, request
app = Flask(__name__)
@app.route("/greet")
def greet():
    fmt = request.args.get("fmt", "{name}")  # sanitized
    return fmt.format(name="guest")
