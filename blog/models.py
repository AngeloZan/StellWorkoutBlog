from django.db import models
from slugify import slugify
from account.models import Account
import os
import uuid

CATEGORIAS_POSTS = (
    ('nenhuma', 'Nenhuma'),
    ('primeiros_passos', 'Primeiros Passos'),
    ('movimentos', 'Movimentos'),
    ('treinos', 'Treinos'),
    ('alimentacao', 'Alimentação'),
    ('descanso', 'Descanso'),
)

def wrapper(instance, filename):
    # Funcao utilizada por Post
    ext = filename.split('.')[-1]
    filename = '{}-{}.{}'.format(slugify(instance.title), uuid.uuid4(), ext)
    return os.path.join('posts', filename)


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    intro = models.TextField(verbose_name='Introdução')
    file = models.FileField(upload_to=wrapper, verbose_name='Arquivo')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=25, default='nenhuma', choices=CATEGORIAS_POSTS, verbose_name='Categoria') 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']


