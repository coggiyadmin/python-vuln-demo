"""SAFE mirror — cache_probe.py; Vary:* body not stored in app cache."""
from flask import Flask, Response, make_response, request

app = Flask(__name__)


@app.route("/profile")
def profile_no_cache():
    resp = make_response({"email": request.headers.get("X-User-Email", "user@example.com")})
    resp.headers["Vary"] = "*"
    resp.headers["Cache-Control"] = "no-store, private"
    return resp


@app.route("/profile/cached")
def profile_serve():
    return Response(b"{}", mimetype="application/json")
