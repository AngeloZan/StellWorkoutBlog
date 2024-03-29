# This is not actually my code
# You can check https://www.youtube.com/playlist?list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW
# I used this course to build my account app

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from PIL import Image
from uuid import uuid4
import os
from django_countries.fields import CountryField

GENDER_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Prefiro não dizer'),
)

def wrapper(instance, filename):
    # Funcao utilizada por Profile
    ext = filename.split('.')[-1]
    filename = '{}_{}.{}'.format(instance.pk, uuid4().hex, ext)
    return os.path.join('profile_pics', filename)

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Usuários precisam ter um endereço de e-mail.')
        if not username:
            raise ValueError('Usuários precisam ter um username.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email                   = models.EmailField(max_length=60, unique=True, error_messages={'unique':"Já existe uma conta com este email."})
    username                = models.CharField(verbose_name="nome de usuário", max_length=30, unique=True)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    dark_mode               = models.BooleanField(default=False)
    date_of_birth           = models.DateField(blank=True, null=True, verbose_name='nascimento')
    name                    = models.CharField(blank=True, max_length=60, verbose_name='nome')
    country                 = CountryField(blank=True, verbose_name='país')
    gender                  = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, verbose_name='gênero')

    # email stuff
    confirmed               = models.BooleanField(default=False)
    subscriber              = models.BooleanField(default=True)
    notificacoes            = models.CharField(default='', max_length=200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'conta'
        verbose_name_plural = 'contas'




