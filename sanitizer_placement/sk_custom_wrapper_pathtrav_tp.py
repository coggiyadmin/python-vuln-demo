"""C1 custom wrapper — org helper strips leading slash only."""
import os
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.lstrip("/")

@app.route("/f")
def f():
    p = company_sanitize(request.args.get("p", ""))
    open("/data/" + p)
