import re
import ldap
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/l")
def l():
    uid = request.args.get("uid", "")
    if not uid or len(uid) > 64:
        abort(400)
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", uid):
        abort(403)
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")
