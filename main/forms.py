from django import forms
from main import models

class ArticleForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset = models.Author.objects.all())
    class Meta:
        model = models.Article
        fields = ('title', 'content','authors')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'