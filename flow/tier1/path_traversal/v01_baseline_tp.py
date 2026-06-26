from flask import Flask, request
app = Flask(__name__)
@app.route("/r")
def r():
    p = request.args.get("p", "")  # SOURCE
    return open("/data/" + p).read()  # SINK CWE-22
