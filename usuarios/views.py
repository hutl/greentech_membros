from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UsuarioCreationForm
from django.views.generic import ListView, DeleteView, CreateView
from .models import *

class AltIndexView (ListView):
   model = Usuario
   template_name= "altindex.html"
   context_object_name = 'users'

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qtd_usuario'] = Usuario.objects.count()
        return context

class CriarContaView(CreateView):
    form_class = UsuarioCreationForm
    success_url = reverse_lazy('usuarios:altindex')  # Redirecionar para a página de login após o registro
    template_name = 'criar_user.html'  # O nome do template para exibir o formulário de 
    
class DeletarContaView(DeleteView):
    model = Usuario
    template_name = 'deletar.html'
    success_url = reverse_lazy('usuarios:altindex')