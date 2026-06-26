from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")[0:999]
    return "<p>" + t + "</p>"  # PRP-05 slice
