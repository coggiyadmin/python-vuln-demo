"""Combination #9 — COMMENT / STRING-LITERAL × LDAP (CWE-90, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    u = request.args.get("user", "")
    # conn.search_s(BASE, ldap.SCOPE_SUBTREE, "(uid=" + u + ")")
    example = "(uid=" + u + ")"  # string only, not executed as filter
    return str(len(example))

