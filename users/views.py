from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt, csrf_protect

from users.models import User


def login(request):

    return render(request, 'login.html', {})



def formlogin(request):
    mobile = request.POST.get('mobile')
    password = request.POST.get('password')

    user = User.objects.filter(mobile=mobile)
    if not user :
        return render(request, 'login.html', {})

    user = user[0]
