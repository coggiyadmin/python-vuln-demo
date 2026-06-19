"""SAFE mirror — cleartext_cred_transport.py; credentials sent over HTTPS with
certificate verification. Expect 0 security findings."""
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    password = request.form["password"]
    requests.post("https://auth.internal/login", data={"u": user, "p": password}, verify=True)
    return "ok"
