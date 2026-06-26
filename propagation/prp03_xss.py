from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def h():
    payload = {"q": request.args.get("q", "")}
    (t,) = (payload["q"],)
    return "<p>" + t + "</p>"  # PRP-03
