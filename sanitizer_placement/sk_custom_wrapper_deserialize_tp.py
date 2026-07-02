"""C1 custom wrapper — org helper strips 'pickle' only."""
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace('pickle', '')

@app.route('/d', methods=['POST'])
def d():
    blob = request.get_data()
    safe = company_sanitize(blob.decode('latin1', errors='replace'))
    import pickle; pickle.loads(safe.encode('latin1'))
