from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import  login, logout
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(type(user))
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()

    context = {
        'form':form
    }
    return render(request, 'account/signup.html',context)


def login_view(request):
    if request.method == 'POST':
        print(request)
        print(request.POST)
        print(type(request.POST))
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            print('----------------next Url-----------------')
            print(request.POST.get('next'))
            if request.POST.get('next') :
                return redirect(request.POST['next'])
            return HttpResponseRedirect(reverse('home'))
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
