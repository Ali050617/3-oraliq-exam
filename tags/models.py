from django.db import models
from posts.models import Post
from posts.base_models import BaseModels


class Tag(BaseModels):
    name = models.CharField(max_length=50, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.name

