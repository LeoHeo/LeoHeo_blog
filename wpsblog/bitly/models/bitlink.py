from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from hashids import Hashids


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


def post_save_bitlink(sender, instance, created, **kwargs):
    if created:
        hash_ids = Hashids(salt="bitlink", min_length=4)
        instance.shorten_hash = hash_ids.encode(instance.id)
        instance.save()

post_save.connect(post_save_bitlink, sender=BitLink)
