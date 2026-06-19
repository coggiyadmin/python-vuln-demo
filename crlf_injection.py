"""CWE-93 — CRLF Injection. User input with CR/LF written into a response header
splits the response / injects headers. (Engine gap — cf #86/113.) FN probe."""
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/track")
def track():
    val = request.args.get("v", "")   # SOURCE
    resp = make_response("ok")
    resp.headers["X-Track"] = val      # CR/LF in val injects/splits headers → CWE-93
    return resp
