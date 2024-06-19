from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print(request.path)
    return render(request,'home/home.html')

@login_required
def homeMenu(request,name):
    print(request.path)
    pageDetails={'details':name}
    return render(request,'home/menu.html',pageDetails)