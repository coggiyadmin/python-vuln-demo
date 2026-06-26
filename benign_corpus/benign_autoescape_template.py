"""TN — Jinja2 autoescape enabled."""
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(loader=PackageLoader("app", "templates"), autoescape=select_autoescape(["html"]))
def render(name: str) -> str:
    return env.get_template("hello.html").render(name=name)
