"""IL-33 — .env style config → shell (IL-5)."""
import os
import subprocess

def run_from_env() -> None:
    cmd = os.environ.get("RUN_CMD", "")  # SOURCE config/env
    subprocess.call(cmd, shell=True)  # SINK CWE-78
