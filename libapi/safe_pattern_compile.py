"""TN — re.compile on constant pattern, not user code (#124)."""
import re

PAT = re.compile(r"^[a-zA-Z0-9]+$")

def matches(user: str) -> bool:
    return bool(PAT.match(user))
