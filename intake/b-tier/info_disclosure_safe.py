"""Safe mirror — PAT-INFO-01"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/debug")
def debug():
    return jsonify({"status": "ok"})
