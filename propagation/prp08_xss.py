from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def h():
    t = ""
    try:
        t = request.args.get("q", "")
    except Exception:
        pass
    return "<p>" + t + "</p>"  # PRP-08
