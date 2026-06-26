import sqlite3
def public_query(name: str) -> None:
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + name + "'")
