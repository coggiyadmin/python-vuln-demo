from flask import Flask, request
from ldap3 import Connection
app = Flask(__name__)
@app.route("/d")
def d():
    dn = request.args.get("dn", "")
    Connection("ldap://localhost").search(dn, "(objectClass=*)")  # SINK CWE-90
