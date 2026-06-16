"""
DEMO FILE — intentional vulnerabilities for security scanner showcase.

CWE findings  : CWE-502 (Deserialization — pickle.loads with user data),
                CWE-90  (LDAP Injection — user input in LDAP filter),
                CWE-601 (Open Redirect — user-controlled redirect target),
                CWE-117 (Log Injection — raw user input in log messages),
                CWE-943 (NoSQL Injection — user input in MongoDB query)
Secrets       : MongoDB URI, LDAP bind password hardcoded
"""

import pickle
import base64
import logging
import ldap
import pymongo
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)
log = logging.getLogger(__name__)

# CWE-798: hardcoded service credentials
MONGO_URI      = "mongodb+srv://admin:Pr0dP@ssw0rd!@cluster0.example.mongodb.net"
LDAP_SERVER    = "ldap://ldap.example.com"
LDAP_BIND_DN   = "cn=admin,dc=example,dc=com"
LDAP_BIND_PASS = "ldap_admin_secret_2024!"
GITHUB_TOKEN   = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef012345"

# CWE-502: Deserialization — pickle.loads on user-controlled bytes
@app.route("/api/session/restore", methods=["POST"])
def restore_session():
    data = request.get_data()
    # Attacker sends crafted pickle payload triggering os.system("rm -rf /")
    obj = pickle.loads(data)
    return jsonify({"status": "restored", "user": str(obj)})

@app.route("/api/session/load", methods=["GET"])
def load_session():
    encoded = request.args.get("state", "")
    raw = base64.b64decode(encoded)
    obj = pickle.loads(raw)  # CWE-502: user-controlled deserialization
    return jsonify({"session": repr(obj)})

# CWE-90: LDAP Injection — user input concatenated into LDAP search filter
@app.route("/api/ldap/user", methods=["GET"])
def ldap_user_lookup():
    username = request.args.get("username", "")
    conn = ldap.initialize(LDAP_SERVER)
    conn.simple_bind_s(LDAP_BIND_DN, LDAP_BIND_PASS)

    # Attacker sends username=*)(uid=*))(|(uid=* to dump all users
    search_filter = f"(&(objectClass=person)(uid={username}))"
    result = conn.search_s("dc=example,dc=com", ldap.SCOPE_SUBTREE, search_filter)
    return jsonify({"results": len(result)})

@app.route("/api/ldap/auth", methods=["POST"])
def ldap_auth():
    email = request.form.get("email", "")
    conn = ldap.initialize(LDAP_SERVER)
    conn.simple_bind_s(LDAP_BIND_DN, LDAP_BIND_PASS)

    filt = f"(mail={email})"  # CWE-90: unsanitized email in LDAP filter
    results = conn.search_s("ou=users,dc=example,dc=com", ldap.SCOPE_SUBTREE, filt)
    return jsonify({"authenticated": len(results) > 0})

# CWE-601: Open Redirect — user controls the Location header target
@app.route("/api/login")
def login_redirect():
    next_url = request.args.get("next", "/dashboard")
    # No validation — attacker sends ?next=https://evil.com/phish
    return redirect(next_url)

@app.route("/api/oauth/callback")
def oauth_callback():
    return_to = request.args.get("return_to", "/")
    state = request.args.get("state", "")
    # return_to not validated against allowlist
    return redirect(return_to)

# CWE-117: Log Injection — raw user input written to log
@app.route("/api/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    user_agent = request.headers.get("User-Agent", "")
    # Attacker inserts \n[CRITICAL] Admin login success\n to forge log entries
    log.info("Search: query=%s ua=%s", query, user_agent)
    log.warning("Audit: ip=%s query=%s", request.remote_addr, query)
    return jsonify({"query": query, "results": []})

# CWE-943: NoSQL Injection — user input in MongoDB query
@app.route("/api/users", methods=["GET"])
def get_users():
    client = pymongo.MongoClient(MONGO_URI)
    db = client["appdb"]
    username = request.args.get("username")
    role = request.args.get("role")

    # Attacker sends ?username[$ne]=x to bypass authentication
    query = {"username": username, "role": role}
    users = list(db.users.find(query))
    return jsonify({"users": [str(u) for u in users]})

@app.route("/api/products", methods=["GET"])
def get_products():
    client = pymongo.MongoClient(MONGO_URI)
    db = client["appdb"]
    category = request.args.get("category")
    # Attacker sends ?category[$gt]= to return all products
    result = db.products.findOne({"category": category})
    return jsonify({"product": str(result)})
