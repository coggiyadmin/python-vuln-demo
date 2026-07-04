# v09 guard-in-variable — column allowlist in module set.
import sqlite3

ALLOWED_COLS = frozenset({"name", "email"})

def lookup(col: str, val: str) -> None:
    if col in ALLOWED_COLS:
        sqlite3.connect(":memory:").execute(f"SELECT {col} FROM users WHERE {col}=?", (val,))
