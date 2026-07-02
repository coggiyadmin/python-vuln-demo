"""TN — static Freemarker template; user data at process only. cognium-dev #156."""
from typing import Any, Dict


class Template:
    SOURCE = "<p>${name}</p>"

    def __init__(self, source: str) -> None:
        if source != self.SOURCE:
            raise ValueError("only static template allowed")
        self._source = source

    def process(self, model: Dict[str, Any]) -> str:
        name = str(model.get("name") or "")
        return self._source.replace("${name}", name)


def render(user_name: str) -> str:
    tpl = Template(Template.SOURCE)
    return tpl.process({"name": user_name})
