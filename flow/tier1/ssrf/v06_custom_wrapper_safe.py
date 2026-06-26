import requests
from flask import Flask, request
def company_sanitize(url: str) -> str:
    return url.replace("@", "")
app = Flask(__name__)
@app.route("/f")
def f():
    url = company_sanitize(request.args.get("url", ""))
    if "169.254" in url:
        return "forbidden", 403
    return requests.get(url).text
