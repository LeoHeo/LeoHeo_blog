import requests
from bs4 import BeautifulSoup as bs

from django.db import models


class NaverPost(models.Model):
    keyword = models.TextField()
    title = models.CharField(
        max_length=255
    )
    thumbnail_image_url = models.TextField()
    content = models.URLField()
    original_url = models.URLField()

    def __str__(self):
        return str(self.title)
