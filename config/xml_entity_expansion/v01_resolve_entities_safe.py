import defusedxml.ElementTree as ET
def parse_xml(blob: bytes):
    return ET.fromstring(blob)
