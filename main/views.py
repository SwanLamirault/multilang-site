from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .models import FormulaireArticle
from django.utils.translation import activate
from django.http import HttpResponseRedirect
from django.conf import settings

# Create your views here.

def liste_articles(request):
    articles = Article.objects.all()
    print("articles : " + str(articles))
    return render(request, 'listeArticles.html', {'articles': articles})


def article(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'article.html', {'article': article})

def ajout_article(request):
    if request.method == 'POST': # On s'assure que c'esr bien un POST
        form = FormulaireArticle(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = FormulaireArticle()

    return render(request, 'ajout_article.html', {'form' : form})

def supprimer_article(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        article.delete()
        return redirect('liste_articles')  # On retourne à la liste des articles
    return render(request, 'article.html', {'article': article})


def changer_langue(request, language_code):
    activate(language_code)
    next_url = request.POST.get('next', '/')
    response = HttpResponseRedirect(next_url)
    response.set_cookie(settings.LANGUAGE_CODE, language_code)
    return redirect('/' + str(language_code))