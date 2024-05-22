from django.shortcuts import render

from user.models import User


# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    re_password = request.POST['re-password']

    user = User(username=username, email=email, password=password)

    user.save()

    return render(request, 'register.html')
