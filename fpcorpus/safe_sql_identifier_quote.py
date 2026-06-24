"""FP-target (cognium-dev#163, py) — SQL identifier validated against an allowlist regex and
quoted; value bound as a parameter. Must not be flagged sql_injection."""
import re
import sqlite3
def by_column(conn: sqlite3.Connection, column: str, value: str):
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", column):
        raise ValueError("bad identifier")
    return conn.execute(f'SELECT * FROM items WHERE "{column}" = ?', (value,)).fetchall()
