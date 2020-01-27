from django.db import models
from article.models import Article
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    answer = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True, blank=True)
