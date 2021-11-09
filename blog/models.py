from django.db import models
from slugify import slugify


def wrapper(instance, filename):
    # Funcao utilizada por Post
    ext = filename.split('.')[-1]
    filename = '{}-{}.{}'.format(instance.pk, slugify(instance.title), ext)
    return os.path.join('posts', filename)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        