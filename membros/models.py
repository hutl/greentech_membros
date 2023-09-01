from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from datetime import datetime

class Membro (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nasc = models.DateField(verbose_name='Data de Nascimento')
    curso = models.CharField(max_length=200, default='CST em Análise e Desenvolvimento de Sistemas')
    media_curso = models.DecimalField(max_digits=3, decimal_places=2)
    foto = models.ImageField(upload_to='uploads/',default='')

    def calcular_idade(self):
        hoje = datetime.now().date()
        idade = hoje.year - self.data_nasc.year - ((hoje.month, hoje.day) < (self.data_nasc.month, self.data_nasc.day))
        return idade

    def __str__(self):
        return self.nome
    
class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField(verbose_name='Data de Nascimento')
    email = models.EmailField()
    password = models.CharField(max_length=50, default='')
    USERNAME_FIELD = "email"

    @staticmethod
    def create_user(username,  password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is None:
            extra_fields['is_staff'] = False
        if extra_fields.get('is_superuser') is None:
            extra_fields['is_superuser'] = False

        password = make_password(password)
        return Usuario._default_manager.create(username=username, password=password, **extra_fields)
