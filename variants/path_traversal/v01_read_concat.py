from flask import Flask, request, send_file
app = Flask(__name__)
@app.route("/f")
def f():
    name = request.args.get("name", "")
    return send_file("/var/data/" + name)  # SINK CWE-22
