from django.shortcuts import render, redirect
from django.urls import reverse
from users.models import User
from django.contrib import auth
from users.backends import CustomBackend
from setting.models import *
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password']:
            try:
                user = User.objects.get(username=request.POST['name'])
                return render(request, r'helpdesk\authentication\templates\signup.html', {'error': 'Username has already been taken!'})
            except:
                user = User.objects.create_user(
                    username=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
                auth.login(request, user,
                           backend='django.contrib.auth.backends.ModelBackend')
                return redirect('/account')

        else:
            return render(request, r'helpdesk\authentication\templates\signup.html', {'error': 'paswords did not match!'})
    else:
        return render(request, r'helpdesk\authentication\templates\signup.html')


def signin(request):
    if request.method == 'POST':

        user = CustomBackend.authenticate(request,
                                          username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
            try:
                userRole = UserRole.objects.get(user=user)
                return redirect('/account/ExpertAccount')
            except:
                return redirect('/account')
        else:
            return render(request, r'helpdesk\authentication\templates\signin.html', {'error': 'Invalid Username Or Password'})
    else:
        return render(request, r'helpdesk\authentication\templates\signin.html')


def logout(request):
    logout(request)
    return redirect(reverse("users:login"))
