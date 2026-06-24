"""FP-target (#128/#140) — LIBRARY profile. Public utility; `cmd` is caller-supplied."""
import subprocess


def run(cmd: str):
    return subprocess.run(cmd, shell=True, capture_output=True)  # caller-supplied, not attacker source
