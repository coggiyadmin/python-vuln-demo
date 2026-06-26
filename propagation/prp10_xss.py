from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def h():
    parts = []
    for x in request.args.getlist("q"):
        parts.append(x)
    t = "".join(parts)
    return "<p>" + t + "</p>"  # PRP-10 collect
