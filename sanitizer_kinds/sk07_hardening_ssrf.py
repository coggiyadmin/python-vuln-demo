import xml.etree.ElementTree as ET
def parse_xml(raw: bytes):
    parser = ET.XMLParser()
    return ET.fromstring(raw, parser=parser)  # SK-07 XXE hardening TN
