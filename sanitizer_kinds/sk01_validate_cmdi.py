from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/x")
def h():
    n = request.args.get("n", "")
    if not n.isalnum():
        abort(400)
    import sqlite3
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + n + "'")  # SK-01 validate partial
