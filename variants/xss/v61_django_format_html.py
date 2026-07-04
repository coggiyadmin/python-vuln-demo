from django.http import HttpResponse
from django.utils.html import format_html
def view(request):
    name = request.GET.get("name", "")
    return HttpResponse(format_html("<div>{}</div>", name).format(name) + name)  # SINK CWE-79 unescaped concat
