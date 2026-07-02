"""C1 wrong-context — HTML escape before format string."""
import html
from flask import Flask, request
app = Flask(__name__)
@app.route("/greet")
def greet():
    fmt = html.escape(request.args.get("fmt", "{name}"))
    return fmt.format(name="guest")
