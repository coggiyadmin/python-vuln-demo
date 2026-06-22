"""IL-5 config-driven boundary — SAFE mirror of interop_yaml_gadget.py.
Uses yaml.safe_load, which only constructs plain scalars/lists/dicts and cannot
instantiate arbitrary Python objects. ZERO security findings expected.
"""
import yaml

from flask import Flask, request

app = Flask(__name__)


@app.route("/config", methods=["POST"])
def load_config():
    blob = request.data  # SOURCE (untrusted YAML document)
    # Safe: safe_load forbids arbitrary object tags — `!!python/object/...` raises.
    cfg = yaml.safe_load(blob)
    return str(cfg)
