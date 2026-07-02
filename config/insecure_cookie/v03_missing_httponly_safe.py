from flask import make_response
def set_sid(resp, sid):
    resp.set_cookie('SESSIONID', sid, secure=True, httponly=True, samesite='Lax')
