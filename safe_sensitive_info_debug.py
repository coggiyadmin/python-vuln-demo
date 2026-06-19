"""SAFE mirror — sensitive_info_debug.py; the debug branch returns only a correlation id."""
import logging
import uuid
from flask import Flask

app = Flask(__name__)
log = logging.getLogger("app")


@app.route("/op")
def op():
    try:
        raise RuntimeError("boom")
    except RuntimeError:
        ref = uuid.uuid4().hex
        log.exception("op failed ref=%s", ref)  # detail stays server-side
        return "error ref=" + ref, 500
