"""TP (CWE-614/1004) — cookie set without Secure/HttpOnly."""
from flask import make_response
def login():
    resp = make_response("ok")
    resp.set_cookie("SESSIONID", "abc", secure=False, httponly=False)  # SINK (CWE-614/1004)
    return resp
