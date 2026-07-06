"""Tool implementations wired into the agent by runner.py (LLM06 — part 2 of 3)."""
import subprocess


def run_shell(command: str) -> str:
    # Executes whatever the agent decides to pass — bounded only by the (unrestricted)
    # scopes declared in agent_config.yaml. No validation, no allowlist.
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout
