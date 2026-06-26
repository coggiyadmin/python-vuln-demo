import sqlite3
def plugin_query(name: str) -> None:
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + name + "'")
