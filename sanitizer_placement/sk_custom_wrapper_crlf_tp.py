"""C1 custom wrapper — org helper strips '\r' only."""
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace('\r', '')

from flask import make_response
@app.route('/go')
def go():
    nxt = company_sanitize(request.args.get('next', ''))
    resp = make_response('ok')
    resp.headers['Location'] = '/home?u=' + nxt
    return resp
