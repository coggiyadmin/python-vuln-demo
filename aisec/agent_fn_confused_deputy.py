"""Excessive Agency FN probe (OWASP LLM06) — confused-deputy via tool. Each tool call
looks individually scoped, but the agent forwards the user's privileged token to a
model-chosen internal URL, letting prompt-controlled input reach internal services
(SSRF / IDOR through the agent). Expected: trust layer MISS.
"""
import os

import requests

INTERNAL_TOKEN = os.environ.get("SERVICE_TOKEN", "")


def fetch_tool(url: str) -> str:
    # SINK (LLM06 confused-deputy): model-chosen url + ambient privileged token.
    # No allowlist on host → http://169.254.169.254/... or internal admin API reachable.
    return requests.get(url, headers={"Authorization": f"Bearer {INTERNAL_TOKEN}"}).text


TOOLS = [{"name": "fetch", "description": "Fetch a URL on behalf of the user", "fn": fetch_tool}]
