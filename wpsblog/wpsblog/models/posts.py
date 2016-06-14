import os

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ModelForm


class PostManager(models.Manager):
    def public(self):
        return self.filter(is_public=True)


class Post(models.Model):
    objects = PostManager()

    user = models.ForeignKey(User)

    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()
    is_public = models.BooleanField(
        default=True
    )
    image = models.ImageField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post:detail",
            kwargs={
                "pk": self.id,
            }
        )

    def get_update_url(self):
        return reverse(
            "post:update",
            kwargs={
                "pk": self.id
            }
        )

    def get_image_url(self):
        if self.image:
            return self.image.url
        return "http://placehold.it/350x150"
