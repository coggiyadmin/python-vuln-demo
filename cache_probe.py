"""FN probe — CWE-524 improper cache of response with Vary:* (FN-09)."""
from flask import Flask, Response, make_response, request

app = Flask(__name__)
_cache: dict[str, bytes] = {}


@app.route("/profile")
def profile_cached():
    resp = make_response({"email": request.headers.get("X-User-Email", "private@corp.io")})
    resp.headers["Vary"] = "*"
    resp.headers["Cache-Control"] = "no-store"
    key = f"profile:{request.headers.get('Authorization', 'anon')}"
    _cache[key] = resp.get_data()  # CWE-524
    return resp


@app.route("/profile/cached")
def profile_serve():
    key = f"profile:{request.headers.get('Authorization', 'anon')}"
    return Response(_cache.get(key, b"{}"), mimetype="application/json")
