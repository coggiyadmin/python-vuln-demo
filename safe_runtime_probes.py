"""
NEGATIVE TEST FILE — safe mirrors of runtime_probes.py patterns.

The scanner MUST produce ZERO security findings here. Any finding is a
FALSE POSITIVE.
"""

import hashlib
import hmac
import subprocess
import urllib.request
from pathlib import Path

from flask import Flask, request, Response, make_response, jsonify

app = Flask(__name__)

PATCH_ROOT = Path("/tmp/patches").resolve()
WORKTREE_ROOT = Path("/var/repos/worktree").resolve()
ALLOWED_BUNDLE_HOSTS = {"cdn.example.com"}
BUNDLE_SIGNING_KEY = b"demo-hmac-key-not-for-production"


def register_hooks() -> None:
    """Explicit opt-in registration — no import-time side effects."""
    return None


# SAFE supply chain — no module-level credential harvest on import.


# SAFE download — host allowlist + HMAC signature check; shell=False argv list.
@app.route("/import-dropper", methods=["POST"])
def import_dropper():
    url = request.args.get("bundle", "")
    signature = request.args.get("sig", "")
    parsed = urllib.request.urlparse(url)
    if parsed.hostname not in ALLOWED_BUNDLE_HOSTS:
        return "forbidden host", 403
    expected = hmac.new(BUNDLE_SIGNING_KEY, url.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        return "invalid signature", 403
    tmp = Path("/tmp") / "signed-stage.pyz"
    urllib.request.urlretrieve(url, tmp)
    subprocess.run(["python3", str(tmp)], check=False, shell=False)
    return "ok"


# SAFE path — filename slugified; resolved path must stay under PATCH_ROOT.
@app.route("/git/format-patch", methods=["POST"])
def git_format_patch():
    subject = request.form.get("subject", "patch")
    slug = "".join(c if c.isalnum() or c in "-_" else "-" for c in subject)[:64]
    target = (PATCH_ROOT / f"{slug}.patch").resolve()
    if not str(target).startswith(str(PATCH_ROOT) + "/"):
        return "forbidden", 403
    target.write_text(request.form.get("body", ""))
    return str(target)


# SAFE path — entry resolved and prefix-checked under WORKTREE_ROOT.
@app.route("/git/checkout", methods=["POST"])
def git_checkout():
    entry = request.form.get("path", "")
    dest = (WORKTREE_ROOT / entry).resolve()
    if not str(dest).startswith(str(WORKTREE_ROOT) + "/"):
        return "forbidden", 403
    dest.parent.mkdir(parents=True, exist_ok=True)
    blob = request.files["blob"].read()
    written = dest.write_bytes(blob)
    return jsonify({"path": str(dest), "bytes": written})


# SAFE cache — Vary:* responses are not stored in the app cache.
@app.route("/profile")
def profile_no_cache():
    resp = make_response({"email": request.headers.get("X-User-Email", "user@example.com")})
    resp.headers["Vary"] = "*"
    resp.headers["Cache-Control"] = "no-store, private"
    return resp


@app.route("/profile/cached")
def profile_serve():
    return Response(b"{}", mimetype="application/json")
