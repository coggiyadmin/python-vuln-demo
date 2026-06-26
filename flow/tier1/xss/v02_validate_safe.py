from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/s")
def s():
    q = request.args.get("q", "")
    if len(q) > 32 or "<" in q or ">" in q: abort(400)
    return "<h1>" + q + "</h1>"
