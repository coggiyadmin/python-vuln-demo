# v10 allowlist-set — XXE hardening feature flag
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as DET
def parse(raw: bytes):
    return DET.fromstring(raw)
