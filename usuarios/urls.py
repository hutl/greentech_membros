from django.urls import path
from .views import *

app_name = 'usuarios'
urlpatterns = [
    path('',AltIndexView.as_view(), name="altindex"),
    path('criar/',CriarContaView.as_view(), name="criar"),
    path('deletar/<int:pk>',DeletarContaView.as_view(), name="deletar"),
]