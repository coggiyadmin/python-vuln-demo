from django.http import HttpResponse
from django.contrib.auth.models import User
def view(request):
    name = request.GET.get("name", "")
    users = User.objects.raw("SELECT * FROM auth_user WHERE username = '%s'" % name)  # SINK CWE-89 Django .raw()
    return HttpResponse(str(list(users)))
