from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def go_view(request):
    nxt = request.GET.get("next", "")
    return redirect(nxt)  # SINK CWE-601 Django redirect shortcut
