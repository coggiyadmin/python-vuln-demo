"""C1 hardening — isinstance gate only; pickle still unsafe."""
import pickle
from flask import Flask, request
app = Flask(__name__)
@app.route("/d", methods=["POST"])
def d():
    blob = request.get_data()
    if not isinstance(blob, (bytes, bytearray)):
        return "bad", 400
    pickle.loads(blob)
