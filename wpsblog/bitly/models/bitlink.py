from django.db import models
from django.core.urlresolvers import reverse


class BitLink(models.Model):
    origin_url = models.URLField()
    shorten_hash = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )
    created_by = models.DateField(auto_now_add=True)
    updated_by = models.DateField(auto_now=True)

    def __str__(self):
        return self.origin_url

    def get_absolute_url(self):
        pass
