"""C1 wrong-context — SQL quote escape before Location header."""
import sqlite3
from flask import Flask, request, Response
app = Flask(__name__)
@app.route("/redir")
def redir():
    loc = request.args.get("url", "").replace("'", "''")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + loc + "'")
    resp = Response("redirecting")
    resp.headers["Location"] = loc
    return resp
