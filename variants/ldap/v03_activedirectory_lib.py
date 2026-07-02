from flask import Flask, request
from ldap3 import Server, Connection, ALL
app = Flask(__name__)
@app.route("/u")
def u():
    user = request.args.get("user", "")
    Connection(Server("ldap://localhost", get_info=ALL), user="cn=admin", password="x").search(
        "ou=users", "(sAMAccountName=" + user + ")")  # SINK CWE-90 ldap3 pool
