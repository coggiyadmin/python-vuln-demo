"""
DEMO FILE — patterns from famous SAST benchmarks not yet exercised.

Aligns with:
  OWASP Benchmark  : crypto, hash, weakrand categories
  Bandit           : B303 (MD5), B304/305 (weak cipher), B311 (random),
                     B501 (request_with_no_cert_validation), B323 (unverified ctx)
  CWE              : CWE-327, CWE-328, CWE-330, CWE-295

These are constant-algorithm / config-flag vulnerabilities (NOT taint-driven) —
they require pattern detection, not source→sink flow.
"""

import hashlib
import random
import ssl
import requests
import urllib3


# CWE-328 / Bandit B303 — MD5 for security (constant algorithm, no taint)
def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()  # weak hash


# CWE-327 — SHA1 (constant algorithm)
def fingerprint(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()  # weak hash


# CWE-330 / Bandit B311 — non-crypto RNG for a security token
def make_reset_token() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(6))  # weak random


# CWE-295 / Bandit B501 — TLS certificate verification disabled
def fetch_insecure(url: str):
    return requests.get(url, verify=False)  # cert validation OFF → MITM


# CWE-295 / Bandit B323 — unverified SSL context
def open_socket(host: str, port: int):
    ctx = ssl._create_unverified_context()  # disables cert + hostname checks
    return ctx


# CWE-295 — disabling urllib3 warnings to hide the insecure transport
def fetch_no_warn(url: str):
    urllib3.disable_warnings()
    return requests.get(url, verify=False)
