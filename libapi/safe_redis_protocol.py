"""FP-target (upstream cognium-dev#170, py, CRITICAL) — execute_command issues a RESP *protocol*
verb (GET/SET), never an OS command. Must not be flagged command_injection (CWE-78)."""


def cache_get(client, key: str):
    # `client` is a redis client; execute_command sends a wire-protocol verb, not an OS exec.
    return client.execute_command("GET", key)  # protocol verb, NOT OS exec
