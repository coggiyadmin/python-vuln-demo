from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api/public')
def public():
    resp = jsonify({'ok': True})
    resp.headers['Access-Control-Allow-Origin'] = '*'  # SINK CWE-942
    return resp
