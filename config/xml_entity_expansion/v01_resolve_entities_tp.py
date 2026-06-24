import xml.etree.ElementTree as ET
def parse_xml(blob: bytes):
    return ET.fromstring(blob, ET.XMLParser(resolve_entities=True))  # SINK CWE-776
