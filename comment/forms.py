from django import forms
from . models import Comment
class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('answer',)
