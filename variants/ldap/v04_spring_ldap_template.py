from flask import Flask, request
from ldap3 import Server, Connection
app = Flask(__name__)
@app.route("/ldap")
def ldap():
    user = request.args.get("user", "")
    Connection(Server("ldap://localhost"), user="cn=admin", password="x").search(
        "ou=users", f"(uid={user})")  # SINK CWE-90 f-string filter
