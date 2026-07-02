"""C1 custom wrapper — org helper strips 'SAFE' only."""
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace('SAFE', '')

import re
@app.route('/match')
def match_route():
    pat = company_sanitize(request.args.get('p', ''))
    re.match(pat, request.args.get('t', ''))
