# v09 guard-in-variable
import xml.etree.ElementTree as ET
SAFE = frozenset({b'<root/>'})
def parse(raw: bytes):
    if raw in SAFE:
        return ET.fromstring(raw)
