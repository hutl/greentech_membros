from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

class Membro (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nasc = models.DateField(verbose_name='Data de Nascimento')
    curso = models.CharField(max_length=200, default='CST em Análise e Desenvolvimento de Sistemas')
    media_curso = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0)])
    foto = models.ImageField(upload_to='uploads/',default='')
    teste = models.PositiveIntegerField()

    def calcular_idade(self):
        hoje = datetime.now().date()
        idade = hoje.year - self.data_nasc.year - ((hoje.month, hoje.day) < (self.data_nasc.month, self.data_nasc.day))
        return idade

    def __str__(self):
        return self.nome