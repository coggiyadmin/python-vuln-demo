"""C1 wrong-context — HTML escape before path read."""
from flask import Flask, request
import html
app = Flask(__name__)
@app.route("/f")
def f():
    p = html.escape(request.args.get("p", ""))
    open("/data/" + p).read()
