"""Demo-tree TP (CWE-89) — intentional vuln under sample/ for --exclude-demos gate."""
import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/demo")
def demo():
    q = request.args.get("q", "")  # SOURCE
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + q + "'")  # SINK CWE-89
