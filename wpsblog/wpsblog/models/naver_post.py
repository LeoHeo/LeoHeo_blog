import requests
from bs4 import BeautifulSoup as bs

from django.db import models


class NaverPost(models.Model):
    title = models.TextField()
    thumbnail_image_url = models.TextField()
    content = models.TextField()
    original_url = models.TextField()

    def __str__(self):
        return str(self.title)
