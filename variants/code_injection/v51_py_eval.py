from flask import Flask, request
app = Flask(__name__)
@app.route("/v")
def v():
    expr = request.args.get("expr", "")
    return str(eval(expr))  # SINK CWE-94 eval user expr
