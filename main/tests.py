from django.test import TestCase

# Create your tests here.
from .models import Article
from django.utils import timezone

Article.objects.create(title='Premier Article', content='Contenu du premier article', publication_date=timezone.now())
Article.objects.create(title='Deuxième Article', content='Contenu du deuxième article', publication_date=timezone.now())
