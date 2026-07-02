"""C1 wrong-context — SQL escape before eval."""
from flask import Flask, request
app = Flask(__name__)
@app.route("/e")
def e():
    expr = request.args.get("q", "").replace("'", "''")
    eval(expr)
