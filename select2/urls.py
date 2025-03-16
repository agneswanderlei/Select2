from django.urls import path
from .views import PessoasCreateView, home

urlpatterns = [
    path('pessoas/create/', PessoasCreateView.as_view(), name='pessoas_create'),
    path('pessoas/add/', home, name='pessoas_add' )
]
