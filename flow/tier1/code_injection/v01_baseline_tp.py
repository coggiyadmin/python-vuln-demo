from flask import Flask, request
app = Flask(__name__)
@app.route("/e")
def e():
    x = request.args.get("x", "")  # SOURCE
    return str(eval(x))  # SINK CWE-94
