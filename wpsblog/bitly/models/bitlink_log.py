from django.db import models


class BitLinkLog(models.Model):
    bitlink = models.ForeignKey("BitLink")

    http_referer = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    http_user_agent = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    http_remote_address = models.CharField(
        max_length=31,
        blank=True,
        null=True,
    )

    http_meta_json = models.TextField(blank=True, null=True)

    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
