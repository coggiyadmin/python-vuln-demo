"""c08 SAFE — custom wrapper × LDAP (CWE-90). Expect clean."""
import re
import ldap
from flask import Flask, request, abort

app = Flask(__name__)


def checked_uid(uid):
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", uid):
        abort(400)
    return uid


@app.route("/wrapped")
def wrapped():
    uid = checked_uid(request.args.get("uid", ""))
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")
