"""Improper Output Handling (OWASP LLM05) — model output spliced into a SQL string. The
LLM is asked to produce a WHERE clause that is concatenated into a query, so injected
content reaches the database verbatim. TP-2.
"""
import sqlite3

from openai import OpenAI

client = OpenAI()


def search(nl_query: str):
    clause = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"SQL WHERE clause for: {nl_query}"}],
    ).choices[0].message.content
    conn = sqlite3.connect("app.db")
    # SINK (LLM05 -> SQLi): model output concatenated into the query
    return conn.execute("SELECT * FROM items WHERE " + clause).fetchall()
