"""
NEGATIVE TEST FILE — safe mirror of setup.py install-time exfiltration.

The scanner MUST produce ZERO security findings here. Any finding is a
FALSE POSITIVE.
"""

from setuptools import setup, find_packages

setup(
    name="python-vuln-demo-safe-setup",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[],
)
