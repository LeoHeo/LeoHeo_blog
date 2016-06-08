import os

from django.db import models
from django.core.urlresolvers import reverse

from django.conf import settings


class PostManager(models.Manager):
    def public(self):
        return self.filter(is_public=True)


class Post(models.Model):
    objects = PostManager()

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
                "post_id": self.id,
            }
        )

    def get_update_url(self):
        return reverse(
            "post:update",
            kwargs={
                "post_id": self.id
            }
        )
