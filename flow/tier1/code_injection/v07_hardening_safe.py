from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/e")
def e():
    x = request.args.get("x", "")
    if x not in {"0", "1", "2"}:
        abort(403)
    return str(int(x))  # hardening — no eval
