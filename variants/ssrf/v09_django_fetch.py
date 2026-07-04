from django.http import HttpResponse
import urllib.request
def proxy_view(request):
    url = request.GET.get("url", "")
    return HttpResponse(urllib.request.urlopen(url).read())  # SINK CWE-918 Django view
