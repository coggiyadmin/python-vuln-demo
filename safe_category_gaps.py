"""SAFE mirror — category_gaps.py hardened CRLF, mass-assignment (#86).

CSRF (CWE-352) graduated to safe_csrf.py; unrestricted upload (CWE-434) to
safe_unrestricted_upload.py.
"""
import secrets
from flask import Flask, Response, jsonify, request

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


class Account:
    def __init__(self):
        self.balance = 0
        self.is_admin = False


ALLOWED_PROFILE_FIELDS = frozenset({"display_name", "timezone"})


@app.route("/redir")
def redir():
    loc = request.args.get("url", "")
    if "\r" in loc or "\n" in loc:
        return Response("bad", status=400)
    resp = Response("redirecting")
    resp.headers["Location"] = loc
    return resp


@app.route("/profile", methods=["POST"])
def profile():
    acct = Account()
    for k, v in request.form.items():
        if k in ALLOWED_PROFILE_FIELDS:
            setattr(acct, k, v)
    return jsonify({"admin": acct.is_admin})
