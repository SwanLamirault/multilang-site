from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', include('main.urls')),  # Incluez ici vos URLs de l'application 'main'
]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),  # Incluez à nouveau vos URLs de 'main' pour les différentes langues
)
