"""IL-5 config-driven boundary — SAFE mirror of interop_env_to_eval.py.
The config value is parsed as a number, never evaluated as code. ZERO findings.
"""
import os


def compute_quota():
    raw = os.environ.get("QUOTA", "0")  # SOURCE (config value)
    # Safe: parse as an integer — config data treated strictly as data, no eval.
    try:
        return int(raw)
    except ValueError:
        return 0
