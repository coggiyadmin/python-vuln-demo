# v09 guard-in-variable — tag allowlist held in module variable.
ALLOWED_TAGS = frozenset({"p", "span"})

def render(tag: str, text: str) -> str:
    if tag in ALLOWED_TAGS:
        return f"<{tag}>{text}</{tag}>"
    return "<p>blocked</p>"
