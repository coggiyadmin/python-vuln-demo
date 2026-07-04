# v10 allowlist-set
from jinja2 import Environment, BaseLoader, select_autoescape
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(['html']))
def render(name: str):
    return env.from_string('<p>{{ n }}</p>').render(n=name)
