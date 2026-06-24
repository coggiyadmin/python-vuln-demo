"""FN/FP-target (elarasu cognium-dev#128/#169, #140 Python port) — LIBRARY profile. A reusable
helper; `where` is caller-supplied, not an HTTP entry point. With an entry-point gate this must
NOT be sql_injection (no attacker-reachable source)."""
import sqlite3


def by_filter(conn: sqlite3.Connection, where: str):
    return conn.execute("SELECT * FROM items WHERE " + where).fetchall()  # caller-supplied, not entry point
