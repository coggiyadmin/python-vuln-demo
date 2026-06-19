"""CWE-183 — Permissive List of Allowed Inputs. The host allow-check uses substring
containment, so `evil-trusted.com.attacker.net` passes. Real vuln; NO finding = FN."""
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/fetch")
def fetch():
    target = request.args.get("url", "")   # SOURCE
    if "trusted.com" in target:            # overly-permissive substring allow-list → CWE-183
        return redirect(target)
    return "blocked", 400
