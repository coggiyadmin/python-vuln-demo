"""FP-target (cognium-ai#109/#123) — assert guard must not become exploitable sqli."""


def lookup(conn, user_id: int):
    assert user_id is not None
    return conn.execute("SELECT * FROM u WHERE id=?", (user_id,))
