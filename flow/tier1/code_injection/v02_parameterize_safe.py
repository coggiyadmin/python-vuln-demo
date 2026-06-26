from flask import Flask, request
app = Flask(__name__)
LOOKUP = {"0": 0, "1": 1, "2": 2}
@app.route("/e")
def e():
    return str(LOOKUP.get(request.args.get("x", ""), 0))
