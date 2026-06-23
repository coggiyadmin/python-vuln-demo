"""TN — benign template fill (no AI-attack surface). Builds a notification string
from validated, typed fields; no model call, no instruction assembly.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Notice:
    user: str
    amount: int


def render(notice: Notice) -> str:
    if notice.amount < 0:
        raise ValueError("amount must be non-negative")
    return f"Hi {notice.user}, your balance changed by {notice.amount} credits."
