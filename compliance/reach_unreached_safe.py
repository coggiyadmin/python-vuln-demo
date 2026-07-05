# SAFE — pyyaml imported but the vulnerable API is never called (unreachable)
import yaml

def dump_config(cfg: dict) -> str:
    return yaml.safe_dump(cfg)  # only safe API used; yaml.load never reached
