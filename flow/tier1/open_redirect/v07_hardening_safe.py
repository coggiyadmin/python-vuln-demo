from flask import Flask, request, redirect, abort
app = Flask(__name__)
@app.route("/go")
def go():
    nxt = request.args.get("next", "")
    if not nxt.startswith("/"):
        abort(403)
    return redirect(nxt)
