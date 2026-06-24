"""FP-target (upstream cognium-dev#165, py) — plugin discovery via importlib.metadata entry
points loads classes declared in trusted installed-package metadata, not from user input. Not
reflection injection."""
from importlib.metadata import entry_points


def discover_plugins():
    plugins = []
    for ep in entry_points(group="demo.plugins"):  # trusted package metadata, not user input
        plugins.append(ep.load())  # SPI load from installed dist-info
    return plugins
