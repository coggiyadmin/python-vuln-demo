import pickle
from flask import Flask, request
app = Flask(__name__)
@app.route("/p", methods=["POST"])
def p():
    blob = request.get_data()
    pickle.loads(blob)  # SINK CWE-502
