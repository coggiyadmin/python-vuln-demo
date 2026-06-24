import pickle
from flask import Flask, request
app = Flask(__name__)
@app.route("/v", methods=["POST"])
def v():
    import code
    snippet = request.get_data(as_text=True)
    code.InteractiveInterpreter().runsource(snippet)  # SINK CWE-94
