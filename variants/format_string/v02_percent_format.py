from flask import Flask, request
app = Flask(__name__)
@app.route("/p")
def p():
    msg = request.args.get("msg", "")
    return ("%s" % msg)  # SINK CWE-134
