"""TN — library public API; caller supplies bound params (#169)."""
from typing import Any

def run_query(conn: Any, sql: str, params: tuple) -> Any:
    return conn.execute(sql, params)
