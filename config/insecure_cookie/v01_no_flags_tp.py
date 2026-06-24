from flask import make_response
def set_sid(resp, sid):
    resp.set_cookie('SESSIONID', sid, secure=False, httponly=False)  # SINK CWE-614
