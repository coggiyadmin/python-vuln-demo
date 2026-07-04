from flask import Flask, request
import jsonpickle
app = Flask(__name__)
@app.route("/d", methods=["POST"])
def d():
    return jsonpickle.decode(request.get_data(as_text=True))  # SINK CWE-502 jsonpickle
