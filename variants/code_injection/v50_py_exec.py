from flask import Flask, request
app = Flask(__name__)
@app.route("/e")
def e():
    code = request.args.get("code", "")
    exec(code)  # SINK CWE-94 exec user code
    return "ok"
