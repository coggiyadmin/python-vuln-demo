"""C1 framework-native bypass — SQLAlchemy text() with concat."""
from sqlalchemy import create_engine, text
from flask import Flask, request
app = Flask(__name__)
@app.route("/q")
def q():
    n = request.args.get("n", "")
    create_engine("sqlite://").connect().execute(text("SELECT * FROM u WHERE n='" + n + "'"))
