"""SAFE mirror (OWASP LLM06) — filesystem tool jailed to a workspace dir with a
resolved-path prefix check; any path escaping the jail is rejected before I/O.
"""
from pathlib import Path

WORKSPACE = Path("/var/app/workspace").resolve()


def _resolve(rel_path: str) -> Path:
    target = (WORKSPACE / rel_path).resolve()
    if not target.is_relative_to(WORKSPACE):
        raise PermissionError("path escapes workspace jail")
    return target


def read_tool(rel_path: str) -> str:
    return _resolve(rel_path).read_text()


def write_tool(rel_path: str, content: str) -> None:
    _resolve(rel_path).write_text(content)
