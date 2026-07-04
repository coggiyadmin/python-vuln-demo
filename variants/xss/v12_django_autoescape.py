from django.template import Context, Template
from django.http import HttpRequest
def django_render(req: HttpRequest):
    q = req.GET.get("q", "")  # SOURCE
    return Template("{{ q }}").render(Context({"q": q}))  # SINK CWE-79 — autoescape ON but |safe bypass risk
