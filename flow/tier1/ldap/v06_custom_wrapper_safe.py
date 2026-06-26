# custom_wrapper mirror — ldap
import re
import ldap
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/l")
def l():
    uid = request.args.get("uid", "")
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", uid):
        abort(403)
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")
