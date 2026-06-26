from flask import Flask, request, abort
from markupsafe import escape
app = Flask(__name__)
@app.route("/s")
def s():
    q = request.args.get("q", "")
    if len(q) > 32:
        abort(400)
    return f"<h1>{escape(q)}</h1>"
