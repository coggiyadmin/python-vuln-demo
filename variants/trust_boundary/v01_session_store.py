# trust_boundary variant: Flask session store.
from flask import Flask, session, request
app = Flask(__name__)
@app.route("/role")
def role():
    session["role"] = request.args.get("role", "")  # SINK CWE-501
