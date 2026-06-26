import sqlite3
def lookup(n: str) -> None:
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n=?", (n,))  # SK-03 TN
