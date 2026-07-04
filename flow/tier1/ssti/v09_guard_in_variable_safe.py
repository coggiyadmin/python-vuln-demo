# v09 guard-in-variable
from jinja2 import Environment, BaseLoader
ALLOWED = frozenset({'Hello {{ name }}'})
env = Environment(loader=BaseLoader(), autoescape=True)
def render(tmpl: str, ctx: dict):
    if tmpl in ALLOWED:
        return env.from_string(tmpl).render(**ctx)
