from django.db import models
from django import forms
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField()

class FormulaireArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'publication_date']
        widgets = {
            'publication_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }