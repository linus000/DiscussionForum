from django.shortcuts import render, redirect
from .forms import ArticleCreationForm
from django.contrib.auth.decorators import login_required

import comment.models as cModels
import comment.forms as  cForms

from .models import Article
# Create your views here.
from django.contrib.auth.models import User

@login_required(login_url='account/login')
def create_article(request):
    if request.method == 'POST':
        form = ArticleCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
        return redirect('home')
    else:
        form = ArticleCreationForm()
    context = {'form' : form}
    return render(request, 'article/creation.html', context)


def delete_article(request):
    pass


def update_article(request):
    pass


def article_list(request):
    article = Article.objects.order_by('-publish_date')
    context = {
        'article':article
    }
    return render(request, 'article/view.html',context)


def detailed_article(request, title):
    detailed_article = Article.objects.get(title=title)
    comments = cModels.Comment.objects.filter(article=detailed_article)
    cform = cForms.CommentCreationForm()
    context = {
        'detailed_article': detailed_article,
        'comments': comments,
        'cform':cform

    }
    return render(request, 'article/detail.html', context)
