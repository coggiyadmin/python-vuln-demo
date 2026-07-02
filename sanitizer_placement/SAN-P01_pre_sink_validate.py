"""SAN-P01 — validate before sink (pre-sink placement)."""
import re
import sqlite3

def lookup(user: str) -> None:
    if not re.fullmatch(r"[a-zA-Z0-9]+", user):
        return
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + user + "'")
