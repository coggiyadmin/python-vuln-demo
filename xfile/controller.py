"""Cross-file taint — the SOURCE side. Flask handler that passes user input
into a sink defined in db_helper.py. The scanner MUST trace taint across the
import boundary; if no finding is produced, cross-file taint is a FALSE NEGATIVE.
"""
from flask import Flask, request

from db_helper import run_user_query, run_command

app = Flask(__name__)


@app.route("/user")
def user():
    name = request.args.get("name", "")   # SOURCE
    return str(run_user_query(name))       # → db_helper.run_user_query sink (CWE-89)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")    # SOURCE
    run_command(host)                      # → db_helper.run_command sink (CWE-78)
    return "ok"
