from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def h():
    v = request.cookies.get("pref", "")  # SOURCE SRC-04 cookie
    return "<p>" + v + "</p>"  # SINK CWE-79
