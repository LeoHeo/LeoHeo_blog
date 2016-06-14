from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class BitLink(models.Model):
    user = models.ForeignKey(User)

    origin_url = models.URLField()
    shorten_hash = models.CharField(
        max_length=8,
        blank=True,
        null=True
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.origin_url

    def get_absolute_url(self):
        return reverse("home")
