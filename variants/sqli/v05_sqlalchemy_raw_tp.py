"""SQLi variant — SQLAlchemy text() string concat (TP)."""
from sqlalchemy import create_engine, text
from flask import request

engine = create_engine("sqlite:///:memory:")
def bad():
    uid = request.args.get("id", "")
    with engine.connect() as conn:
        conn.execute(text("SELECT * FROM users WHERE id=" + uid))  # SINK CWE-89
