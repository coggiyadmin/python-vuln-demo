"""Combination #5 — OOP OBJECT FLOW × XXE (CWE-611, Python). Taint injected via
__init__, stored on self, parsed with entity resolution enabled (directly and via
a property). Each is a REAL XXE; NO finding = FALSE NEGATIVE."""
import lxml.etree as ET
from flask import Flask, request

app = Flask(__name__)


class Importer:
    def __init__(self, xml):
        self.xml = xml                      # constructor-injected taint

    @property
    def payload(self):
        return self.xml                     # property exposes tainted field

    def parse_direct(self):
        parser = ET.XMLParser(resolve_entities=True, no_network=False)  # external entities ON
        return ET.fromstring(self.xml.encode(), parser)                 # 5a → XXE sink (CWE-611)

    def parse_via_property(self):
        parser = ET.XMLParser(resolve_entities=True, no_network=False)
        return ET.fromstring(self.payload.encode(), parser)             # 5b via property → sink (CWE-611)


@app.route("/import")
def imp():
    i = Importer(request.args.get("xml", ""))  # SOURCE → constructor
    i.parse_direct()
    i.parse_via_property()
    return "ok"
