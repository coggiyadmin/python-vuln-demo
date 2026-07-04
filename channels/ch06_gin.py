"""CH-06 Gin-style redirect param → open redirect."""
from flask import Flask, request, redirect
app = Flask(__name__)
@app.route("/go")
def go():
    return redirect(request.args.get("next", ""))  # SINK CWE-601
