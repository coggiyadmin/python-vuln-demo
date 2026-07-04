# v10 allowlist-set — parameterized query after value allowlist gate.
import sqlite3

SAFE_IDS = {1, 2, 3}

def lookup(user_id: int) -> None:
    if user_id in SAFE_IDS:
        sqlite3.connect(":memory:").execute("SELECT * FROM users WHERE id=?", (user_id,))
