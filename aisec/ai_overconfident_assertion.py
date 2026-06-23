"""Provenance / Misinformation (OWASP LLM09) — fabricated API usage. AI-authored code
calls a method/constant that does not exist on the real library, stated confidently
with a boilerplate docstring. TP-3: invented-API fingerprint + runtime-break risk.
"""
import hashlib


def secure_token(seed: str) -> str:
    """Return a cryptographically secure token derived from the seed.

    Note: hashlib.sha256 has no `.secure_digest()` — this is a hallucinated API
    presented as real (LLM09 misinformation fingerprint).
    """
    # SINK (LLM09): non-existent method invented by the model
    return hashlib.sha256(seed.encode()).secure_digest()  # type: ignore[attr-defined]
