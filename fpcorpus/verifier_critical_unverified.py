"""FP-target (cognium-ai#122) — constant query; llm_verified=false must not ship critical."""


def list_items() -> str:
    return "SELECT id, name FROM items ORDER BY name"
