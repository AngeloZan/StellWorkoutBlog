from django.db import models
from slugify import slugify
from account.models import Account
from PIL import Image
import os
import uuid

POST_IMAGE_ASPECT_RATIO = 1.4479 # height / width
POST_IMAGE_MAX_WIDTH = 250 # largura max da imagem do post (em px)

def wrapper(instance, filename):
    # wrapper para o arquivo (pdf) do post
    ext = filename.split('.')[-1]
    filename = '{}-{}.{}'.format(slugify(instance.title), uuid.uuid4(), ext)
    return os.path.join('posts', filename)

def image_wrapper(instance, filename):
    # wrapper para o arquivo de imagem do post
    ext = filename.split('.')[-1]
    filename = '{}-{}.{}'.format(slugify(instance.title), uuid.uuid4(), ext)
    return os.path.join('post_images', filename)


class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name='Nome')
    readable_name = models.CharField(max_length=25, verbose_name='Nome legível')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.readable_name

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    intro = models.TextField(verbose_name='Introdução')
    file = models.FileField(upload_to=wrapper, verbose_name='Arquivo')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)
    image = models.ImageField(default='post_images/default.png', upload_to=image_wrapper, verbose_name='Imagem')
    favourite = models.ManyToManyField(Account, related_name='favourite', blank=True)

    def save(self, *args, **kwargs):
        # corrigindo o tamanho da imagem ao salvar
        super().save()

        img = Image.open(self.image.path)

        width = img.width

        if width > POST_IMAGE_MAX_WIDTH:
            width = POST_IMAGE_MAX_WIDTH # tamanho max permitido para as imagens

        output_size = (width, width*POST_IMAGE_ASPECT_RATIO)
        img.thumbnail(output_size)
        img.save(self.image.path)

    def delete(self, using=None, keep_parents=False):
        self.file.storage.delete(self.file.name)
        self.image.storage.delete(self.image.name)
        super().delete()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']


   
