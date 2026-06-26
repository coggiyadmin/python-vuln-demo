from flask import Flask, request
app = Flask(__name__)
DB = {"1": "<img onerror=alert(1)>"}
@app.route("/show")
def h():
    row = DB.get(request.args.get("id", ""), "")  # SOURCE SRC-09 stored
    return row  # SINK CWE-79
