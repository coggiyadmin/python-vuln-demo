"""SAFE mirror — oop_xxe.py; the parser disables entity resolution, DTD loading
and network access, so external entities cannot be expanded. Expect 0 findings."""
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)


class Importer:
    def __init__(self, xml):
        self.xml = xml

    def parse_direct(self):
        # hardened parser: no entity resolution, no DTD, no network
        parser = ET.XMLParser(resolve_entities=False, no_network=True, load_dtd=False)
        return ET.fromstring(self.xml.encode(), parser)


@app.route("/import")
def imp():
    i = Importer(request.args.get("xml", ""))
    i.parse_direct()
    return "ok"
