from django.db import models
from slugify import slugify
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
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        