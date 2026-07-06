"""Retrieval step — fetches external content the agent will consume (LLM01 indirect, part 1 of 2)."""
import requests


def fetch(url: str) -> str:
    return requests.get(url).text   # SOURCE: untrusted external page content
