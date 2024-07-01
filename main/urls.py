from django.urls import path
from . import views

urlpatterns = [
    path('changer_langue/<str:language_code>/', views.changer_langue, name='changer_langue'),
    path('', views.liste_articles, name='liste_articles'),
    path('articles/ajout/', views.ajout_article, name='ajout_article'),
    path('article/<int:id>/supprimer', views.supprimer_article, name='supprimer_article'),
    path('article/<int:id>/', views.article, name='article')
]