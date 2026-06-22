"""IL-5 config-driven boundary — Python TOML config → dynamic import (CWE-470).

A module name read from an untrusted TOML config file drives importlib, so config
data selects which code gets loaded and executed (unsafe reflection / dynamic
import). Expected today: FN (config value → importlib not modeled).
"""
import importlib
import tomllib


def load_plugin(config_path):
    with open(config_path, "rb") as f:
        cfg = tomllib.load(f)  # SOURCE (untrusted TOML config)
    plugin_name = cfg["plugin"]["module"]
    # SINK (CWE-470): config-controlled module name drives importlib → arbitrary
    # module load + its import-time side effects execute.
    mod = importlib.import_module(plugin_name)
    return mod.run()
