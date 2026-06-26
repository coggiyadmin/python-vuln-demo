from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def h():
    return "<p>" + request.args.get("q", "") + "</p>"  # PRP-01 inline
