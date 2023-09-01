from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(), name="index"),
    path('alt/',AltIndexView.as_view(), name="altindex"),
    path('alt/criar',CriarContaView.as_view(), name="criaruser"),
    path('segredo/',WandinhaView.as_view(),name="eu"),
    path('membro/<int:pk>',MembroView.as_view(),name='detalhe'),
]