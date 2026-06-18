"""Cross-file taint — SINK side (SSRF). Imported by xf_ssrf_controller.py."""
import requests


def fetch_url(url: str):
    # SINK: `url` arrives tainted across the file boundary → SSRF (CWE-918)
    return requests.get(url)
