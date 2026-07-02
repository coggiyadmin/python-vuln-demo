"""IL-5 config-driven boundary — SAFE mirror of interop_env_to_eval.py.

The config value is parsed as a number, never evaluated as code. ZERO findings.
"""
import os


def compute_quota():
    raw = os.environ.get("QUOTA_FORMULA", "0")
    try:
        return float(raw)
    except ValueError:
        return 0.0
