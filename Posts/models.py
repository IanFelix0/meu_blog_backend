from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

def upload_image_id(isntance,filename):
    return f"{isntance.id_post}{filename}"


class Post(models.Model):
    id_post = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True,null=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'
