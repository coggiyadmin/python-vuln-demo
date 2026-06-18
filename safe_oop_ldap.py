"""SAFE mirror — oop_ldap.py; the tainted value is escaped with
ldap.filter.escape_filter_chars before building the filter. Expect 0 findings."""
import ldap
from ldap.filter import escape_filter_chars
from flask import Flask, request

app = Flask(__name__)
conn = ldap.initialize("ldap://dir.internal")
BASE_DN = "ou=people,dc=example,dc=com"


class Directory:
    def __init__(self, user):
        self.user = user

    def _filter(self):
        return "(uid=" + escape_filter_chars(self.user) + ")"   # escape LDAP metachars

    def search_direct(self):
        return conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, self._filter())


@app.route("/dir")
def directory():
    d = Directory(request.args.get("user", ""))
    d.search_direct()
    return "ok"
