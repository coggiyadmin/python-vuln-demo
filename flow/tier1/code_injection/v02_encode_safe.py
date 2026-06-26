from flask import Flask, request
app = Flask(__name__)
@app.route("/e")
def e():
    x = request.args.get("x", "").replace("__", "")
    return str(eval(x))
