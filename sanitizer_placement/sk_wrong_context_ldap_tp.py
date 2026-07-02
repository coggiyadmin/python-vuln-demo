"""C1 wrong-context — HTML escape before LDAP filter."""
import html
import ldap
from flask import Flask, request
app = Flask(__name__)
@app.route("/l")
def l():
    uid = html.escape(request.args.get("uid", ""))
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")
