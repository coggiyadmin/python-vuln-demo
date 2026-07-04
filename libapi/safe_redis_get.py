"""FP-target (N4 real dep) — redis.Redis.get uses wire protocol, not OS exec (#170)."""
import redis


def cache_get(client: redis.Redis, key: str):
    return client.get(key)  # real redis client API — protocol verb, NOT OS exec
