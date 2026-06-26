"""TP — pip install from user URL (CWE-506). CVE-2026-33634 B-tier class."""
import os
from flask import Flask, request

app = Flask(__name__)


@app.post("/tools/install")
def install():
    url = request.form.get("url", "")
    os.system("pip install " + url)  # SINK CWE-78 / supply_chain
