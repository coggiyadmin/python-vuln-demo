"""Combination #13 — ENCODED PAYLOAD × LDAP (CWE-90, Python)."""
import base64
import ldap
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)
conn = ldap.initialize("ldap://dir.internal")
BASE_DN = "ou=people,dc=example,dc=com"


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    user = base64.b64decode(raw).decode()
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + user + ")")  # CWE-90


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    user = unquote(raw)
    conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, "(uid=" + user + ")")  # CWE-90

