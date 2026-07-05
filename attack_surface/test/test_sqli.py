import os, sqlite3
def test_query():
    q = os.environ.get("Q", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + q + "'")  # SINK — test file
