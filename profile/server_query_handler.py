# Server entry-point sqli (TP) — verifier should keep (#154 shape).
from flask import Flask, request
app = Flask(__name__)
@app.route("/q")
def q():
    user = request.args.get("user", "")  # SOURCE
    return "SELECT * FROM u WHERE n='" + user + "'"  # SINK CWE-89
