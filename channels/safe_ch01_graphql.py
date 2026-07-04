"""TN — GraphQL id bound via parameterized query."""
import sqlite3
def resolve_user(_, info, id):
    if not str(id).isdigit():
        return None
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE id=?", (id,))
