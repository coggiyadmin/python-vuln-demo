"""SAFE mirror — the env secret is used LOCALLY only (to auth an internal client);
nothing sensitive crosses a network boundary. ZERO exfiltration expected.
"""
import os
import requests


def report_metrics(payload: dict):
    api_key = os.environ["INTERNAL_API_KEY"]  # used locally as an auth header only
    # Only non-sensitive `payload` is sent, to a first-party host, authed by the key.
    requests.post("https://api.internal.example.com/metrics",
                  json=payload, headers={"Authorization": f"Bearer {api_key}"})
