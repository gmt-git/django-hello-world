from annoying.decorators import render_to
from django.contrib.auth.models import User


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()
    return {'users': users}
