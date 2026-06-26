from flask import Flask, request
import os
app = Flask(__name__)
@app.route("/f")
def f():
    open("/data/" + request.args.get("p", "")).read()
