# SUPERSEDED by real-dep replacement (INTAKE-56/57 N4) — kept for reference.
"""TN — CLI spec object construction, not shell. cognium-dev #167."""
import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="demo")
    p.add_argument("file")
    return p
