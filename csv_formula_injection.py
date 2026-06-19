"""CWE-1236 — CSV Formula Injection. User input written into a CSV cell that begins
with =, +, -, or @ executes as a formula when opened in a spreadsheet. (Engine gap.)
FN probe — NO finding = potential FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/export")
def export():
    name = request.args.get("name", "")   # SOURCE
    # name = '=cmd|"/c calc"!A1' becomes an executable formula in Excel → CWE-1236
    row = name + ",100\n"
    with open("/var/app/export.csv", "a") as f:
        f.write(row)
    return "exported"
