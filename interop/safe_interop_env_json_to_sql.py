"""SAFE — parameterized lookup."""
import json
import os
import sqlite3

def lookup():
    blob = os.environ.get("USER_FILTER", "{}")
    filt = json.loads(blob).get("name", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n=?", (filt,))
