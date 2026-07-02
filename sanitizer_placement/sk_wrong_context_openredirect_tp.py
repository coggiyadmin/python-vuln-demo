"""C1 wrong-context — HTML escape before redirect."""
import html
from flask import Flask, request, redirect
app = Flask(__name__)
@app.route("/go")
def go():
    nxt = html.escape(request.args.get("next", ""))
    return redirect(nxt)
