"""
CATEGORY-COVERAGE probes — vulnerability classes NOT currently in the engine's
rule set (or under-modeled). Each handler is a REAL vulnerability. Findings that
do NOT fire are coverage gaps (feature requests), documented in CATEGORY_COVERAGE.md.
"""
import logging
import re
import subprocess  # noqa
import traceback
import xml.etree.ElementTree as ET

import jwt
from flask import Flask, request, Response, jsonify

app = Flask(__name__)
log = logging.getLogger("app")


# CWE-352 CSRF graduated to csrf_probe.py + safe_csrf.py (FN-16)
# CWE-434 unrestricted upload graduated to unrestricted_upload_probe.py
#         + safe_unrestricted_upload.py (FN-19)


# CWE-113 — CRLF / HTTP response splitting: user input in a response header
@app.route("/redir")
def redir():
    loc = request.args.get("url", "")
    resp = Response("redirecting")
    resp.headers["Location"] = loc           # CR/LF in `loc` splits the response
    return resp


# CWE-915 — Mass assignment: user-controlled keys set all attributes
class Account:
    def __init__(self): self.balance = 0; self.is_admin = False
@app.route("/profile", methods=["POST"])
def profile():
    acct = Account()
    for k, v in request.form.items():
        setattr(acct, k, v)                  # attacker sets is_admin=true
    return jsonify({"admin": acct.is_admin})


# CWE-1333 — ReDoS: user-controlled regex (or catastrophic pattern on user input)
@app.route("/match")
def match():
    pattern = request.args.get("p", "")
    return jsonify({"m": bool(re.match(pattern, "some-long-input-string"))})  # user regex


# CWE-532 — Sensitive data in logs: password logged in cleartext
@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]; pw = request.form["password"]
    log.info("login attempt user=%s password=%s", user, pw)   # secret in logs
    return "ok"


# CWE-209 — Information exposure: stack trace returned to the client
@app.route("/calc")
def calc():
    try:
        return str(1 / int(request.args.get("n", "0")))
    except Exception:
        return traceback.format_exc(), 500    # leaks internals


# CWE-134 — Format-string: user-controlled format accesses object internals
@app.route("/greet")
def greet():
    fmt = request.args.get("fmt", "{name}")
    return fmt.format(name="guest", config=app.config)  # {config[SECRET_KEY]} leak


# CWE-347/384 — JWT verification disabled
@app.route("/me")
def me():
    token = request.headers.get("Authorization", "")
    data = jwt.decode(token, options={"verify_signature": False})  # accepts forged tokens
    return jsonify(data)


# CWE-776 — XML entity expansion (billion laughs) — no DTD/entity limits
@app.route("/xml", methods=["POST"])
def parse_xml():
    return ET.fromstring(request.get_data()).tag   # entity expansion DoS
