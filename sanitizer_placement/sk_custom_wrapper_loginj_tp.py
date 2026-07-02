"""C1 custom wrapper — org helper strips '\n' only."""
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace('\n', '')

import logging
log = logging.getLogger('app')
@app.route('/auth')
def auth():
    user = company_sanitize(request.args.get('user', ''))
    log.warning('login user=' + user)
