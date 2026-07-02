"""TN — static Velocity template; user data at merge only. cognium-dev #156."""
from typing import Any, Dict


class VelocityContext:
    def __init__(self, data: Dict[str, Any]) -> None:
        self._data = data

    def get(self, key: str) -> Any:
        return self._data.get(key)


class VelocityEngine:
    TEMPLATE = "<p>$name</p>"

    def evaluate(self, ctx: VelocityContext, out: list[str], _log: str, template: str) -> None:
        if template != self.TEMPLATE:
            raise ValueError("only static template allowed")
        name = str(ctx.get("name") or "")
        out.append(template.replace("$name", name))


def render(user_name: str) -> str:
    engine = VelocityEngine()
    ctx = VelocityContext({"name": user_name})
    buf: list[str] = []
    engine.evaluate(ctx, buf, "greet", VelocityEngine.TEMPLATE)
    return buf[0]
