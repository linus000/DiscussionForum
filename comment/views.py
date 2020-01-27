from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . forms import CommentCreationForm
import article.models as aModels

from django.contrib.auth.decorators import  login_required
# Create your views here.

@login_required(login_url='/account/login')
def create_comment(request):
    if request.method == 'GET':
            form = CommentCreationForm(request.GET)
            title = request.GET.get('title')
            article = aModels.Article.objects.get(title=title)
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.article = article
            comment.save()
            url=reverse('article:detail', args=(title,))
            print(url)
            return HttpResponseRedirect(url)
    else:
        return redirect('home')

def update_comment(request):
    pass

def delete_comment(request):
    pass