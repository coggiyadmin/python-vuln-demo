"""TP — missing human oversight flag on automated decision (#EU-AI-Act pattern)."""
def decide(score: float) -> str:
    return "deny" if score > 0.9 else "allow"  # no human review gate
