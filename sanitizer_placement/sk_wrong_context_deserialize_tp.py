"""C1 wrong-context — SQL quote escape before pickle.loads."""
import pickle
from flask import Flask, request
app = Flask(__name__)
@app.route("/load", methods=["POST"])
def load():
    blob = request.get_data().decode("latin-1", errors="replace").replace("'", "''").encode()
    pickle.loads(blob)
