"""CWE-215 — Insertion of Sensitive Information Into Debugging Code. A debug branch returns the
traceback and DB credentials to the client. NO finding = FALSE NEGATIVE."""
import os
import traceback
from flask import Flask

app = Flask(__name__)
DEBUG = os.environ.get("DEBUG") == "1"


@app.route("/op")
def op():
    try:
        raise RuntimeError("boom")
    except RuntimeError:
        if DEBUG:
            # leaks traceback + secrets through a debug path → CWE-215
            return traceback.format_exc() + "\nDB_PASSWORD=" + os.environ.get("DB_PASSWORD", ""), 500
        return "error", 500
