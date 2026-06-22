"""IL-5 config-driven boundary — Python env/config value → eval (CWE-94).

A value sourced from the environment / a config file drives a dangerous code path:
it is passed to eval(), turning config data into executed code. Expected today:
FN (env/config as a taint source not modeled).
"""
import os


def compute_quota():
    # SOURCE: a config value from the environment (set by an untrusted .env/CI var).
    formula = os.environ.get("QUOTA_FORMULA", "0")
    # SINK (CWE-94): config-supplied string evaluated as Python code.
    return eval(formula)
