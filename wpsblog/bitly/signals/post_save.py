from django.db.models.signals import post_save
from django.dispatch import receiver
from hashids import Hashids

from bitly.models import BitLink


@receiver(post_save, sender=BitLink)
def post_save_bitlink(sender, instance, created, **kwargs):
    if created:
        hash_ids = Hashids(salt="bitlink", min_length=4)
        instance.shorten_hash = hash_ids.encode(instance.id)
        instance.save()
