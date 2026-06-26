from flask import Flask, request
app = Flask(__name__)
CACHE = {}
@app.route("/a")
def a():
    CACHE["v"] = request.args.get("q", "")
    return "ok"
@app.route("/b")
def b():
    t = CACHE.get("v", "")
    return "<p>" + t + "</p>"  # PRP-09 stored2
