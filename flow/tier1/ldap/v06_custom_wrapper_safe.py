import ldap
from flask import Flask, request
def company_sanitize(x: str) -> str:
    return x.replace(")", "")
app = Flask(__name__)
@app.route("/l")
def l():
    uid = company_sanitize(request.args.get("uid", ""))
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")
