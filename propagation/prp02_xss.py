from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")  # SOURCE
    u = t
    v = u
    return "<p>" + v + "</p>"  # PRP-02 alias
