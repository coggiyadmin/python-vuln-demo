"""IL-5 config-driven boundary — SAFE mirror of interop_toml_dynimport.py.

Only allowlisted plugin module names from config may be imported. ZERO findings.
"""
import importlib
import tomllib

ALLOWED = frozenset({"plugins.safe_demo", "plugins.metrics"})


def load_plugin(config_path):
    with open(config_path, "rb") as f:
        cfg = tomllib.load(f)
    plugin_name = cfg["plugin"]["module"]
    if plugin_name not in ALLOWED:
        raise ValueError("plugin not allowlisted")
    mod = importlib.import_module(plugin_name)
    return mod.run()
