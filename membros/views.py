from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UsuarioCreationForm
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import *

class IndexView (ListView):
   model = Membro
   template_name= "index.html"
   context_object_name = 'membros'

class AltIndexView (ListView):
   model = Usuario
   template_name= "altindex.html"
   context_object_name = 'users'

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qtd_usuario'] = Usuario.objects.count()
        return context

class MembroView(DetailView):
    model = Membro
    template_name = "membro.html"

class WandinhaView(TemplateView):
    template_name = 'segredo.html'

class CriarContaView(CreateView):
    form_class = UsuarioCreationForm
    success_url = reverse_lazy('altindex')  # Redirecionar para a página de login após o registro
    template_name = 'criar_user.html'  # O nome do template para exibir o formulário de registro