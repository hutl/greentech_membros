from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def _create_user(self, nome, password, is_staff, is_superuser, **extra_fields):
       
        if not nome:
            raise ValueError(('O nome deve ser definido!'))
        user = self.model(nome=nome, is_staff=is_staff, is_active=True, is_superuser=is_superuser, **extra_fields)
        user.password = password
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, nome=None, password=None, **extra_fields):
        return self._create_user(nome, password, False, False, **extra_fields)
    def create_superuser(self, nome, password, **extra_fields):
        user=self._create_user(nome, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100, unique=True)
    data_nasc = models.DateField(verbose_name='Data de Nascimento', null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=128, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nome