"""IL-45 — JSON env blob → SQL string (IL-5 config frontier)."""
import json
import os
import sqlite3

def lookup():
    blob = os.environ.get("USER_FILTER", "{}")  # SOURCE
    filt = json.loads(blob).get("name", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + filt + "'")
