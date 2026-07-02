"""C1 fake — strip // only before redirect."""
from flask import Flask, request, redirect
app = Flask(__name__)
@app.route("/go")
def go():
    nxt = request.args.get("next", "").replace("//", "")
    return redirect(nxt)
