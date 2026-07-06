"""Agent runner — loads the tool registry and dispatches model tool-calls (LLM06 — part 3 of 3).

Excessive agency across files: the `shell` tool is registered from agent_config.yaml with
unrestricted scopes and invoked directly on model-chosen input, so a prompt-injected instruction
reaches process_exec with filesystem + network authority. No single file is exploitable alone —
the config grants the capability, tools.py implements the sink, and this file wires them to the model.
"""
import importlib

import yaml


def build_agent(config_path="agent_config.yaml"):
    cfg = yaml.safe_load(open(config_path))
    registry = {}
    for tool in cfg["tools"]:
        module, fn = tool["handler"].rsplit(".", 1)
        registry[tool["name"]] = getattr(importlib.import_module(module), fn)
    return registry


def dispatch(model_action):
    # model_action = {"tool": "shell", "input": "<attacker-influenceable via prompt injection>"}
    registry = build_agent()
    return registry[model_action["tool"]](model_action["input"])
