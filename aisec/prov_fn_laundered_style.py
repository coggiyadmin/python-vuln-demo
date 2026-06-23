"""Provenance FN probe (OWASP LLM09) — laundered AI authorship. Machine-generated
code with the obvious tells removed (no 'AI-generated' comment, no generic foo/bar,
no TODO placeholders) yet still structurally template-shaped. Fingerprint detectors
keyed on surface markers MISS it. Expected: trust layer MISS.
"""
from typing import Sequence


def compute_weighted_average(values: Sequence[float], weights: Sequence[float]) -> float:
    if len(values) != len(weights):
        raise ValueError("values and weights must be the same length")
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("weights must not sum to zero")
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / total_weight
