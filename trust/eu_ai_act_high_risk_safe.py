"""SAFE — human approval required before enforcement."""
def decide(score: float, approved: bool) -> str:
    if not approved:
        return "pending"
    return "deny" if score > 0.9 else "allow"
