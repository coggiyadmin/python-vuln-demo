# TP — vulnerable API is REACHED: yaml.load without SafeLoader (CVE-2020-1747 class)
import yaml

def parse_config(blob: str):
    return yaml.load(blob)  # SINK reachable vulnerable call
