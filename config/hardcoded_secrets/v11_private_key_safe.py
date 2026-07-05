def load_key(secrets: dict) -> str:
    return secrets['private_key']  # injected from the secrets manager, no literal
