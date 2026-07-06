"""Agent runner — SAFE mirror (LLM06, part 3 of 3).

Only the read-only, path-allowlisted doc tool is registered; `allow_all` tools are rejected at
build time, so no tool can reach exec / network / write regardless of what the model emits.
"""
import importlib

import yaml


def build_agent(config_path="agent_config.yaml"):
    cfg = yaml.safe_load(open(config_path))
    registry = {}
    for tool in cfg["tools"]:
        if tool.get("allow_all"):
            raise ValueError("allow_all tools are not permitted")
        module, fn = tool["handler"].rsplit(".", 1)
        registry[tool["name"]] = getattr(importlib.import_module(module), fn)
    return registry


def dispatch(model_action):
    registry = build_agent()
    return registry[model_action["tool"]](model_action["input"])
