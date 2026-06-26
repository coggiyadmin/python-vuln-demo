import ldap
from flask import Flask, request
app = Flask(__name__)
@app.route("/l")
def l():
    uid = request.args.get("uid", "")  # SOURCE
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")  # SINK CWE-90
