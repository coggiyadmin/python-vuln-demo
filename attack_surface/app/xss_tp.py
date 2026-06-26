from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def x():
    return "<p>" + request.args.get("q", "") + "</p>"
