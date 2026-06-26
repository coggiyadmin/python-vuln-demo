from flask import Flask, request
app = Flask(__name__)
@app.route("/s")
def s():
    q = request.args.get("q", "")  # SOURCE
    return "<h1>" + q + "</h1>"  # SINK CWE-79
