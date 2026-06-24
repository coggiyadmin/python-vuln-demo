from flask import Flask, request
app = Flask(__name__)
@app.route("/e", methods=["POST"])
def e():
    code = request.get_data(as_text=True)
    eval(code)  # SINK CWE-94
