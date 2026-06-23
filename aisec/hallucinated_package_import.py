"""Provenance / Misinformation (OWASP LLM09) — hallucinated dependency. AI codegen
routinely invents plausible-but-nonexistent package names ("slopsquatting" surface):
an attacker can pre-register the hallucinated name and ship malware. TP-2: import of
a fabricated package that does not exist on the index.
"""
# SINK (LLM09): non-existent package an LLM commonly hallucinates for HTTP retries.
import requests_retry_session  # noqa: F401  (fabricated dependency)


def fetch(url: str):
    session = requests_retry_session.build(retries=3)
    return session.get(url)
