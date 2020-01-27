from . models import Article
from django import forms


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description', 'slug')

