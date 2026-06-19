"""SAFE mirror — improper_validation.py; the validator result is enforced before use."""
import re
from flask import Flask, request

app = Flask(__name__)
EMAIL = re.compile(r"^[^@]+@[^@]+\.[^@]+$")


@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email", "")
    if not EMAIL.match(email):             # result enforced
        return "invalid email", 400
    save_subscriber(email)
    return "ok"


def save_subscriber(_email):
    pass
