from flask import Flask, request, redirect
app = Flask(__name__)
@app.route("/r")
def r():
    return redirect(request.args.get("next", ""))  # SINK CWE-601 flask redirect user
