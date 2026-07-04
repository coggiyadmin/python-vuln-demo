from flask import Flask, request
app = Flask(__name__)
@app.route("/f")
def f():
    fmt = request.args.get("fmt", "")
    return fmt % {"k": "v"}  # SINK CWE-134 user-controlled format
