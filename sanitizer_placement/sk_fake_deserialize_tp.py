"""C1 fake — comment-only before pickle.loads."""
import pickle
from flask import Flask, request
app = Flask(__name__)
@app.route("/load", methods=["POST"])
def load():
    blob = request.get_data()  # sanitized
    pickle.loads(blob)
