"""SQLi variant — SQLAlchemy text() with bound param (TN contrast)."""
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///:memory:")
def lookup(user_id: int) -> str:
    with engine.connect() as conn:
        row = conn.execute(text("SELECT name FROM users WHERE id = :id"), {"id": user_id}).fetchone()
    return row[0] if row else ""
