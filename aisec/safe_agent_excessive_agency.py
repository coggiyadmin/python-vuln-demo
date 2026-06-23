"""SAFE mirror (OWASP LLM06). The agent's tool exposes only a fixed allowlist of
parameterized actions — least privilege; the model cannot run arbitrary commands.
"""
import subprocess

_ALLOWED = {
    "disk_free": ["df", "-h"],
    "uptime": ["uptime"],
}


def ops_tool(action: str) -> str:
    argv = _ALLOWED.get(action)        # allowlist → fixed argv, no shell
    if argv is None:
        raise ValueError("action not permitted")
    return subprocess.run(argv, capture_output=True, text=True).stdout


TOOLS = [{"name": "ops", "description": "Run a vetted ops action", "fn": ops_tool}]
