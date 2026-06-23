"""Excessive Agency probe (OWASP LLM06). An agent is wired with an unrestricted
shell tool and no allowlist/human-approval, so the model can run any command.
TP: over-broad tool capability granted to an autonomous agent.
"""
import subprocess


def shell_tool(command: str) -> str:
    # SINK (LLM06): the agent can execute ARBITRARY shell commands the model emits —
    # no allowlist, no confirmation, full host authority.
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout


TOOLS = [{"name": "shell", "description": "Run any shell command", "fn": shell_tool}]
