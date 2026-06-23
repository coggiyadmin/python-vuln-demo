"""Excessive Agency (OWASP LLM06) — over-broad filesystem tool. The agent is granted
read/write rooted at "/" with no path jail, so a model-emitted path can touch any file
on the host. TP-2 for LLM06.
"""
from pathlib import Path

FS_ROOT = Path("/")  # SINK (LLM06): no jail — whole filesystem in scope


def read_tool(rel_path: str) -> str:
    # model-controlled rel_path; "../../etc/shadow" escapes any intended dir
    return (FS_ROOT / rel_path).read_text()


def write_tool(rel_path: str, content: str) -> None:
    (FS_ROOT / rel_path).write_text(content)


TOOLS = [{"name": "fs_read", "fn": read_tool}, {"name": "fs_write", "fn": write_tool}]
