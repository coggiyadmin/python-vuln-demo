# v10 allowlist-set — contextual encode after set membership gate.
from html import escape
SAFE_NAMES = {"alice", "bob"}

def greet(name: str) -> str:
    if name in SAFE_NAMES:
        return "<p>Hello " + escape(name) + "</p>"
    return "<p>unknown</p>"
