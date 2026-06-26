"""B-tier PAT-INFO-01 — debug response leaks env (CWE-200)."""
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/debug")
def debug():
    return jsonify({"token": os.environ.get("API_TOKEN"), "q": request.args.get("q")})  # SINK CWE-200
