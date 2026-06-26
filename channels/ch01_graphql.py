"""CH-01 GraphQL resolver — user arg → SQL sink."""
def resolve_user(_, info, id):
    q = id  # SOURCE graphql arg
    import sqlite3
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE id='" + q + "'")
