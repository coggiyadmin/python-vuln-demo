"""FP-target (upstream cognium-dev#155, py) — a Markdown parser's parse produces HTML/an AST, it
does NOT execute code. Must not be flagged code_injection."""
import markdown


def render(src: str) -> str:
    return markdown.markdown(src)  # AST/HTML build — NOT code execution
