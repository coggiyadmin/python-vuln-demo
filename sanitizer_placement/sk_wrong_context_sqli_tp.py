"""C1 wrong-context — HTML encode before SQL sink."""
import html
import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/q")
def q():
    n = html.escape(request.args.get("n", ""))
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + n + "'")
