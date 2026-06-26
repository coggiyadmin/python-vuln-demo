from flask import Flask, session
app = Flask(__name__)
app.secret_key = "x"
@app.route("/show")
def h():
    v = session.get("msg", "")  # SOURCE SRC-10 session
    return "<p>" + v + "</p>"  # SINK CWE-79
