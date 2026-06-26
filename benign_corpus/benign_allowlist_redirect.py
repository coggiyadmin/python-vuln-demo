"""TN — fixed redirect target."""
from flask import Flask, redirect

app = Flask(__name__)
ALLOWED = {"/dashboard", "/profile"}

@app.route("/go")
def go():
    return redirect("/dashboard")
