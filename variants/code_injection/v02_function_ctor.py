from flask import Flask, request
app = Flask(__name__)
@app.route("/f")
def f():
    expr = request.args.get("expr", "")
    eval(compile(expr, "<s>", "eval"))  # SINK CWE-94
