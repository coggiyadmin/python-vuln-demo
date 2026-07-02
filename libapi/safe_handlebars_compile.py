"""TN — compile static template; user data only at render. cognium-dev #156."""
from jinja2 import Environment

env = Environment(autoescape=True)
TEMPLATE = env.from_string("<p>{{ name }}</p>")

def render(name: str) -> str:
    return TEMPLATE.render(name=name)
