from django.shortcuts import render
from .models import gitUser
from .models import link
from .forms import loginForm
import dataGather
from github import Github
# Create your views here.


#handles page routing
def login(request):
    form = loginForm(request.POST)
    if request.method == 'POST':
        if 'userAdd' in request.POST:
            try:
                name = request.POST['userName']
                #populating database with new info
                currentUser = request.session.get('username')
                currentPass = request.session.get('password')
                g = Github(currentUser, currentPass)
                dataGather.getFollowers(name, g)
                currentUser = dataGather.loginUser(g)
                #get all links
                links = link.objects.all()
                context = {
                    'user' : currentUser,
                    'links': links
                }
                return render(request, 'visual.html', context)
            except:
                currentUser = request.session.get('username')
                currentPass = request.session.get('password')
                g = Github(currentUser, currentPass)
                currentUser = dataGather.loginUser(g)
                links = link.objects.all()
                context = {
                    'user' : currentUser,
                    'links': links
                }
                return render(request, 'visual.html', context)
        else:
            if form.is_valid:
                try:
                    request.session['username'] = form.data['userName']
                    request.session['password'] = form.data['password']
                    request.session.modified = True
                    g = Github(form.data['userName'], form.data['password'])
                    currentUser = dataGather.loginUser(g)
                    #get all links
                    links = link.objects.all()
                    context = {
                        'user' : currentUser,
                        'links': links
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
