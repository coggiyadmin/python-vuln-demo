"""TN — benign human-authored parser. Purposeful naming, real stdlib use, no AI
fingerprint and no AI-attack surface.
"""
from datetime import date


def parse_iso_dates(lines: list[str]) -> list[date]:
    out: list[date] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        out.append(date.fromisoformat(line))
    return out
