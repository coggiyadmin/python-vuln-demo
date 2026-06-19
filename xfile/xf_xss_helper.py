"""Cross-file XSS helper — sink only when called from controller with tainted arg."""


def render_title(title: str) -> str:
    return "<h1>" + title + "</h1>"  # CWE-79 sink
