from django.shortcuts import render
from .models import gitUser
from .models import link
from .forms import loginForm
import dataGather
from github import Github
# Create your views here.


def home(request):
    form = loginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            try:
                print(form.data['userName'])
                print(form.data['password'])
                g = Github(form.data['userName'], form.data['password'])
                print("hello")
                currentUser = dataGather.loginUser(g)
                print(currentUser)
                context = {
                    'user' : currentUser
                }
                return render(request, 'visual.html', context)
            except:
                context = {
                    'form' : form,
                    'errorMes': "Invalid login detais"
                }
                return render(request, 'login.html', context)
    else:
        context = {
            'form' : form
        }
        return render(request, 'login.html', context)
