# Deserialization variant: pickle.loads on user bytes.
import pickle
from flask import Flask, request
app = Flask(__name__)
@app.route("/p", methods=["POST"])
def p():
    pickle.loads(request.get_data())  # SINK CWE-502 pickle
