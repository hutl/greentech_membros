from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(), name="index"),
    path('membro/<int:pk>',MembroView.as_view(),name='detalhe'),
]