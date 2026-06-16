"""Combinations #6/#7/#8 — SANITIZER edge cases (Python).
#6 wrong-context: an xss-sanitizer used before a COMMAND sink → should FIRE.
#7 fake-named: a no-op function called sanitize() → should FIRE.
#8 custom wrapper: wraps a real sanitizer → should NOT fire (FP risk).
"""
import os
import shlex
import markupsafe
from flask import Flask, request

app = Flask(__name__)


# #6 WRONG-CONTEXT — markupsafe.escape removes only XSS taint, not command.
@app.route("/wrongctx")
def wrongctx():
    host = markupsafe.escape(request.args.get("host", ""))  # XSS-escaped
    os.system("echo " + str(host))   # COMMAND sink — escape does NOT mitigate → CWE-78 (should FIRE)


# #7 FAKE SANITIZER — name looks protective but it is a no-op.
def sanitize(x):
    return x                          # does nothing

@app.route("/fake")
def fake():
    host = sanitize(request.args.get("host", ""))
    os.system("echo " + host)         # still tainted → CWE-78 (should FIRE)


# #8 CUSTOM WRAPPER — genuinely safe (wraps shlex.quote); engine likely won't know.
def my_clean(x):
    return shlex.quote(x)             # real shell-escaping inside a custom fn

@app.route("/custom")
def custom():
    host = my_clean(request.args.get("host", ""))
    os.system("echo " + host)         # actually safe → should NOT fire (FP risk)
