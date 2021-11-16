from django.db import models
from slugify import slugify
from account.models import Account
import os
import uuid


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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']
        