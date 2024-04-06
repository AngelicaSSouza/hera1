from django .urls import path
from .views import index, contato, catalago, cadastro

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('catalago', catalago),
    path('cadastro', cadastro),
]