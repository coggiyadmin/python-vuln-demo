from jinja2 import Environment, BaseLoader, select_autoescape
env = Environment(loader=BaseLoader(), autoescape=select_autoescape(["html"]))
def render(name: str) -> str:
    return env.from_string("<p>{{ n }}</p>").render(n=name)  # SK-04 TN
