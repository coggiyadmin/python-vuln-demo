"""C1 custom wrapper — org helper strips parens only before LDAP filter."""
import ldap
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace("(", "").replace(")", "")

@app.route("/l")
def l():
    uid = company_sanitize(request.args.get("uid", ""))
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")
