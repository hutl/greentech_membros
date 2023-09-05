from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from .models import *

class IndexView (ListView):
   model = Membro
   template_name= "index.html"
   context_object_name = 'membros'


class MembroView(DetailView):
    model = Membro
    template_name = "membro.html"

class WandinhaView(TemplateView):
    template_name = 'segredo.html'