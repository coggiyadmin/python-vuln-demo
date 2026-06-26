import pickle
from flask import Flask, request
app = Flask(__name__)
@app.route("/load", methods=["POST"])
def load():
  # wrong: pickle on JSON-shaped route
    return str(pickle.loads(request.get_data()))
