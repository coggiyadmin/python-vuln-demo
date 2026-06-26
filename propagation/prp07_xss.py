from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def h():
    t = (request.args.get("q") or "") if request.args else ""
    return "<p>" + t + "</p>"  # PRP-07
