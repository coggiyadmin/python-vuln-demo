from flask import Flask, request
import ldap
app = Flask(__name__)
@app.route("/l")
def l():
    user = request.args.get("user", "")
    conn = ldap.initialize("ldap://localhost")
    conn.search_s("ou=people", ldap.SCOPE_SUBTREE, "(uid=" + user + ")")  # SINK CWE-90 python-ldap
