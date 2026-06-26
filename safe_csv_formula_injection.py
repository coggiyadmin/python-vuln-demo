"""SAFE mirror — csv_formula_injection.py. Prefix cells with a single quote so
spreadsheet apps treat user input as text, not a formula. Expect 0 security findings."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/export")
def export():
    name = request.args.get("name", "")
    safe = "'" + name if name else ""
    row = safe + ",100\n"
    with open("/var/app/export.csv", "a") as f:
        f.write(row)
    return "exported"
