from django.urls import path
from . views import create_article, delete_article, update_article, article_list, detailed_article

app_name = 'article'
urlpatterns = [
    path('create/', create_article, name='create'),
    path('delete/', delete_article, name='delete'),
    path('update/', update_article, name='update'),
    path('detail/<title>',detailed_article, name='detail')

]
