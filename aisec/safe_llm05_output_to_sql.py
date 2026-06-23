"""SAFE mirror (OWASP LLM05) — model selects an intent; each branch runs a constant,
pre-written parameterized query with the value bound. Model output never becomes SQL syntax.
"""
import sqlite3

from openai import OpenAI

client = OpenAI()


def search(nl_query: str, value: str):
    column = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Which field for: {nl_query}? Reply one word."}],
    ).choices[0].message.content.strip()
    conn = sqlite3.connect("app.db")
    # each sink is a constant literal; the value is always bound as a parameter
    if column == "name":
        return conn.execute("SELECT * FROM items WHERE name = ?", (value,)).fetchall()
    if column == "category":
        return conn.execute("SELECT * FROM items WHERE category = ?", (value,)).fetchall()
    if column == "sku":
        return conn.execute("SELECT * FROM items WHERE sku = ?", (value,)).fetchall()
    raise ValueError("field not allowed")
