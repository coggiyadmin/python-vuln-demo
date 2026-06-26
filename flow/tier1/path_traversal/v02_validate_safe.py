from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/r")
def r():
    p = request.args.get("p", "")
    if ".." in p or p.startswith("/"): abort(400)
    return open("/data/" + p).read()
