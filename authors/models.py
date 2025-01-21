from django.db import models
from django.contrib.auth.models import User
from posts.base_models import BaseModels


class Author(BaseModels):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user
