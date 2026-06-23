"""Prompt Injection — DIRECT (OWASP LLM01). Untrusted user text is concatenated
straight into the system/instruction portion of the prompt, so a user can override
the agent's instructions ("ignore previous instructions and ...").
"""
from openai import OpenAI

client = OpenAI()


def answer(user_question: str) -> str:
    # SINK (LLM01): user text injected into the SYSTEM role — no separation.
    system = "You are a support bot. Follow company policy.\n" + user_question
    resp = client.chat.completions.create(
        model="gpt-4", messages=[{"role": "system", "content": system}])
    return resp.choices[0].message.content
