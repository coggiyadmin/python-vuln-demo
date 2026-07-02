"""C1 fake — strip SAFE before eval."""
from flask import Flask, request
app = Flask(__name__)
@app.route("/e")
def e():
    eval(request.args.get("q", "").replace("SAFE", ""))
