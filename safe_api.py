"""
NEGATIVE TEST FILE — secure equivalents of every vulnerable pattern.

Flows user input through safe APIs to each sink type. The scanner MUST produce
ZERO security findings here. Any finding is a FALSE POSITIVE to be filed
against cognium-dev.

Safe patterns exercised:
  sql_injection   → cursor.execute(sql, params) parameterized
  command_injection → subprocess.run([...], shell=False) with arg list
  path_traversal  → os.path.realpath + prefix check
  deserialization → json.loads / yaml.safe_load (not pickle / yaml.load)
  weak_random     → secrets module (not random)
  open_redirect   → allowlist validation before redirect
"""

import json
import os
import secrets
import sqlite3
import subprocess

import yaml
from flask import Flask, request, redirect, jsonify, abort

app = Flask(__name__)

UPLOAD_ROOT = "/var/app/uploads"
ALLOWED_REDIRECTS = {"/dashboard", "/profile", "/settings"}


# SAFE sql — parameterized query, no f-string concatenation
@app.route("/api/user")
def get_user():
    username = request.args.get("username", "")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))  # parameterized
    return jsonify(cur.fetchall())


# SAFE command — argument list, shell=False, fixed executable
@app.route("/api/ping")
def ping():
    host = request.args.get("host", "")
    # No shell: host is a single argv element, cannot inject extra commands
    result = subprocess.run(
        ["ping", "-c", "3", "--", host],
        capture_output=True, text=True, shell=False, timeout=10,
    )
    return jsonify({"output": result.stdout})


# SAFE path — realpath canonicalization with a prefix check
@app.route("/api/file")
def read_file():
    filename = request.args.get("name", "")
    candidate = os.path.realpath(os.path.join(UPLOAD_ROOT, filename))
    if not candidate.startswith(UPLOAD_ROOT + os.sep):
        abort(403)
    with open(candidate, "r", encoding="utf-8") as fh:
        return fh.read()


# SAFE deserialization — json.loads cannot instantiate arbitrary objects
@app.route("/api/session", methods=["POST"])
def restore_session():
    data = request.get_data(as_text=True)
    obj = json.loads(data)  # safe: no code execution
    return jsonify({"user": obj.get("user")})


# SAFE deserialization — yaml.safe_load (CWE-502 fix #4: not a sink)
@app.route("/api/config", methods=["POST"])
def load_config():
    body = request.get_data(as_text=True)
    cfg = yaml.safe_load(body)  # safe: no arbitrary object construction
    return jsonify({"keys": list(cfg.keys()) if cfg else []})


# SAFE random — secrets module for token generation
@app.route("/api/token")
def make_token():
    return jsonify({"token": secrets.token_urlsafe(32)})


# SAFE redirect — destination validated against an allowlist
@app.route("/api/go")
def go():
    target = request.args.get("next", "/dashboard")
    if target not in ALLOWED_REDIRECTS:
        target = "/dashboard"
    return redirect(target)


# SAFE config — credentials from the environment, nothing hardcoded
def db_url():
    return os.environ["DATABASE_URL"]
