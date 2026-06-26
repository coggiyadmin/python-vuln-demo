from flask import Flask, request
app = Flask(__name__)
@app.route("/e")
def e():
    x = request.args.get("x", "0")
    if x not in {"0", "1", "2"}: return "forbidden", 403
    return str(eval(x))
