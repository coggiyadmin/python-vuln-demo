from flask import Flask
app = Flask(__name__)
@app.after_request
def headers(resp):
    resp.headers['X-Frame-Options'] = 'DENY'
    resp.headers['Content-Security-Policy'] = "frame-ancestors 'none'"
    return resp
