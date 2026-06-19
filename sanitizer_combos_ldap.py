"""Combinations #6/#7/#8 — SANITIZER × LDAP INJECTION (CWE-90, Python)."""
import ldap
import re
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)
conn = ldap.initialize("ldap://dir.internal")
BASE_DN = "ou=people,dc=example,dc=com"


def escape_html(s):
    return escape(str(s))


def sanitize_user(s):
    return s


def ldap_safe(s):
    return re.sub(r"[()=*\\]", "", s)


@app.route("/wrong")
def wrong():
    user = escape_html(request.args.get("user", ""))
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + str(user) + ")")  # CWE-90


@app.route("/fake")
def fake():
    user = sanitize_user(request.args.get("user", ""))
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + user + ")")  # CWE-90


@app.route("/wrapped")
def wrapped():
    user = ldap_safe(request.args.get("user", ""))
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + user + ")")  # expect 0 (#8)

