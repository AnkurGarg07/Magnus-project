
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


def login_view(request):
     if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['Password']
        if not username or not password:
            messages.error(request, 'Please enter both username and password.')
            return render(request, 'Account/login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/index')
        else:
            messages.error(request, 'Invalid username or password.')
     return render(request,'Account/login.html')

def logout_view(request):
    logout(request)
    return redirect('/account/login/')
