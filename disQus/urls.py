"""disQus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from article import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.article_list, name='home'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('account/', include('account.urls')),
    path('article/', include('article.urls')),
    path('comment/', include('comment.urls')),
    path('base', TemplateView.as_view(template_name='base.html'), name='base')

]
