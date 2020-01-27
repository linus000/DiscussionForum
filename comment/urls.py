from django.urls import path
from . views import create_comment, delete_comment, update_comment
app_name = 'comment'
urlpatterns = [
    path('create/', create_comment, name='create'),
    path('delete/', delete_comment, name='delete'),
    path('update/', update_comment, name='update'),
]
