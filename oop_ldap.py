"""Combination #5 — OOP OBJECT FLOW × LDAP INJECTION (CWE-90, Python). Taint
injected via __init__, stored on self, used to build a search filter (directly and
via a property). Each is a REAL LDAP injection; NO finding = FALSE NEGATIVE."""
import ldap
from flask import Flask, request

app = Flask(__name__)
conn = ldap.initialize("ldap://dir.internal")
BASE_DN = "ou=people,dc=example,dc=com"


class Directory:
    def __init__(self, user):
        self.user = user                    # constructor-injected taint

    @property
    def uid(self):
        return self.user                    # property exposes tainted field

    def search_direct(self):
        return conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE,
                             "(uid=" + self.user + ")")   # 5a: field → LDAP sink (CWE-90)

    def search_via_property(self):
        return conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE,
                             "(uid=" + self.uid + ")")    # 5b: via property → sink (CWE-90)


@app.route("/dir")
def directory():
    d = Directory(request.args.get("user", ""))  # SOURCE → constructor
    d.search_direct()
    d.search_via_property()
    return "ok"
