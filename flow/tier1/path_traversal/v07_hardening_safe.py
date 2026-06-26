from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/r")
def r():
    p = request.args.get("p", "")
    if not p.isalnum():
        abort(400)
    return open("/data/" + p).read()
