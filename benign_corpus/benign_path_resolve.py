"""TN — pathlib resolve under root."""
from pathlib import Path

ROOT = Path("/data")

def read(name: str) -> str:
    full = (ROOT / name).resolve()
    if not str(full).startswith(str(ROOT.resolve())):
        raise ValueError("path escape")
    return full.read_text()
