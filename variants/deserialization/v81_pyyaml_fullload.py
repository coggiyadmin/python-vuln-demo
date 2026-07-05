from flask import Flask, request
import yaml
app = Flask(__name__)
@app.route("/d", methods=["POST"])
def d():
    return str(yaml.full_load(request.get_data()))  # SINK CWE-502 full_load constructs objects
