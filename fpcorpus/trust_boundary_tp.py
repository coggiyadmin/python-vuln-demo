"""TP (CWE-501) — untrusted request value written into the trusted session store unvalidated."""
from flask import session, request
def set_role():
    session["role"] = request.args.get("role")  # SINK (CWE-501): user data crosses into trusted store
