"""Combination #11 — FAN-OUT × LDAP (CWE-90, Python)."""
import ldap
from flask import Flask, request

app = Flask(__name__)
conn = ldap.initialize("ldap://dir.internal")
BASE_DN = "ou=people,dc=example,dc=com"


@app.route("/fanout")
def fanout():
    u = request.args.get("u", "")  # SOURCE
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + u + ")")  # sink 1
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(cn=" + u + ")")  # sink 2
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(mail=" + u + ")")  # sink 3

