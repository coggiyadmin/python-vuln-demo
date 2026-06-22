"""IL-5 config-driven boundary — SAFE mirror of interop_toml_dynimport.py.
The config value selects among a fixed allowlist of already-imported modules; it
never drives importlib with an arbitrary name. ZERO security findings expected.
"""
import json
import logging

# Pre-imported, vetted plugins — the only modules that can ever be selected.
_PLUGINS = {"json": json, "logging": logging}


def load_plugin(name: str):
    mod = _PLUGINS.get(name)  # allowlist → already-imported module object
    if mod is None:
        raise ValueError("unknown plugin")
    return mod
