from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from user.forms import LoginForm
from user.models import User


def home(request):
    return render(request, 'home.html')


def login(reqeust):
    if reqeust.method == "GET":
        return render(reqeust, "login.html")
    elif reqeust.method == "POST":
        username = reqeust.POST.get('username', None)
        password = reqeust.POST.get('password', None)
    return render(reqeust, 'login.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        re_password = request.POST.get('re-password', None)

    res_data = {}
    if password != re_password:
        res_data['error'] = '비밀번호가 다릅니다.'
        return render(request, 'register.html', res_data)

    user = User(username=username,
                email=email,
                password=make_password(password)
                )
    user.save()
    return render(request, 'register.html')


