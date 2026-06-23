"""Improper Output Handling FN probe (OWASP LLM05) — deferred execution. The model output
is written to a .py file in one step and imported/run later in a separate step. No single
line shows output->exec, so single-flow scanners MISS the multi-hop sink. Expected: MISS.
"""
import runpy

from openai import OpenAI

client = OpenAI()
PLUGIN = "/var/app/plugins/generated.py"


def stage(task: str):
    code = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write a python module for: {task}"}],
    ).choices[0].message.content
    with open(PLUGIN, "w", encoding="utf-8") as f:
        f.write(code)  # SOURCE: model output persisted as code


def activate():
    # SINK (LLM05 deferred): the staged model output is executed in a later call
    return runpy.run_path(PLUGIN)
