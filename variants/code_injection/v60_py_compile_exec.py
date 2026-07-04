from flask import Flask, request
app = Flask(__name__)
@app.route("/c")
def c():
    src = request.args.get("src", "")
    exec(compile(src, "<user>", "exec"))  # SINK CWE-94 compile+exec user source
    return "ok"
