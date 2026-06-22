"""Framework-idiom benign (WS-5.2) — outbound fetch that LOOKS like SSRF but is safe:
the URL is reconstructed from a fixed base + an HMAC-verified token. ZERO findings.
"""
import hashlib
import hmac
import requests
from flask import request

_BASE = "https://assets.example.com/"
_SECRET = b"server-side-only"


def fetch_asset():
    asset_id = request.args.get("id", "")
    sig = request.args.get("sig", "")
    expected = hmac.new(_SECRET, asset_id.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(sig, expected):
        return "bad signature", 403
    # Host is constant; only a verified, opaque id varies — no SSRF surface.
    return requests.get(_BASE + asset_id).content
