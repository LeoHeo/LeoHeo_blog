from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

from .base import PostBaseView


class PostUpdateView(PostBaseView, UpdateView):
    fields = ["title", "content", "image"]
    template_name = "posts/edit.html"
