"""IL-5 config-driven boundary — Python YAML deserialization gadget (CWE-502).

An untrusted config/data file becomes a code path: yaml.load with the default
(unsafe) Loader instantiates arbitrary Python objects, so a crafted YAML document
(`!!python/object/apply:os.system [...]`) executes code. The data file is the
attack surface — a config boundary, not a normal request param.
"""
import yaml

from flask import Flask, request

app = Flask(__name__)


@app.route("/config", methods=["POST"])
def load_config():
    blob = request.data  # SOURCE (untrusted YAML document)
    # SINK (CWE-502): yaml.load without SafeLoader → arbitrary object instantiation.
    cfg = yaml.load(blob, Loader=yaml.Loader)
    return str(cfg)
