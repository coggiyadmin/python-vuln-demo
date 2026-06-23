"""Prompt Injection — TOOL-OUTPUT (OWASP LLM01). The text a tool returns is fed back
into the model's instruction context without escaping, so an attacker who controls a
tool's output (e.g. a scraped page, a DB row, another agent) can inject directives
that steer the next model turn. TP-3 for LLM01.
"""
from openai import OpenAI

client = OpenAI()


def run_with_tool(user_q: str, tool_result: str) -> str:
    # SOURCE: tool_result is attacker-influenceable (scraped/3rd-party/agent output)
    # SINK (LLM01 tool-output): tool text spliced into the system role with authority.
    system = "You are an assistant. Tool said:\n" + tool_result + "\nNow act on it."
    return client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": user_q}],
    ).choices[0].message.content
