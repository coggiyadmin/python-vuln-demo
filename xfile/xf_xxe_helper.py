"""Cross-file taint — SINK side (XXE). Imported by xf_xxe_controller.py."""
import lxml.etree as ET


def parse(xml: str):
    # SINK: `xml` arrives tainted across the file boundary → XXE (CWE-611)
    parser = ET.XMLParser(resolve_entities=True, no_network=False)
    return ET.fromstring(xml.encode(), parser)
