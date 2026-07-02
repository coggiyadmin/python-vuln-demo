from flask import Flask, request
app = Flask(__name__)
TRUSTED = {}
@app.route('/admin')
def admin():
    role = request.headers.get('X-Forwarded-Role', 'guest')
    TRUSTED[request.remote_addr] = role  # SINK CWE-501 trust client header
    return 'ok'
