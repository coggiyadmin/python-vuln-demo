"""CWE-538 — Insertion of Sensitive Information into Externally-Accessible File. A secret is
written to a web-served static directory. Real vuln; NO finding = FALSE NEGATIVE."""
import os
from flask import Flask

app = Flask(__name__)


@app.route("/export-config")
def export_config():
    # writes the API key into a publicly-served static path → CWE-538
    with open("/var/www/static/config.txt", "w") as f:
        f.write("API_KEY=" + os.environ.get("API_KEY", ""))
    return "exported"
