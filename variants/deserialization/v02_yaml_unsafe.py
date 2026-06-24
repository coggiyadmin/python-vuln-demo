import yaml
from flask import Flask, request
app = Flask(__name__)
@app.route("/y", methods=["POST"])
def y():
    yaml.load(request.get_data(), Loader=yaml.Loader)  # SINK CWE-502
