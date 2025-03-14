from django.urls import path
from .views import PessoasCreateView, EstadosAutocomplete, home

urlpatterns = [
    path('pessoas/create/', PessoasCreateView.as_view(), name='pessoas_create'),
    path('estados-autocomplete/', EstadosAutocomplete.as_view(), name='estados-autocomplete'),
    path('pessoas/add/', home, name='pessoas_add' )
]
