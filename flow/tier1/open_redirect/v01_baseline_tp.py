from flask import Flask, request, redirect
app = Flask(__name__)
@app.route("/go")
def go():
    nxt = request.args.get("next", "")  # SOURCE
    return redirect(nxt)  # SINK CWE-601
