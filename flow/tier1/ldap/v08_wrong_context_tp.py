from html import escape
import ldap
from flask import Flask, request
app = Flask(__name__)
@app.route("/l")
def l():
    uid = escape(request.args.get("uid", ""))  # HTML escape wrong for LDAP
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")
