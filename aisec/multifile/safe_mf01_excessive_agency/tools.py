"""Tool implementations — SAFE mirror, least privilege (LLM06, part 2 of 3)."""
import os

_ALLOWED_ROOT = os.path.abspath("docs")


def read_doc(path: str) -> str:
    full = os.path.abspath(path)
    if not full.startswith(_ALLOWED_ROOT + os.sep):
        raise PermissionError("outside docs/ allowlist")
    with open(full) as f:
        return f.read()
