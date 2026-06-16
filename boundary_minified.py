import sqlite3,flask
app=flask.Flask(__name__)
@app.route("/x")
def x(): u=flask.request.args.get("u","");return str(sqlite3.connect("d").cursor().execute("SELECT * FROM t WHERE c='"+u+"'").fetchall())
