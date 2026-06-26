from flask import Flask, request
app = Flask(__name__)
class Box:
    pass
@app.route("/x")
def h():
    b = Box()
    b.t = request.args.get("q", "")
    return "<p>" + b.t + "</p>"  # PRP-04 field
