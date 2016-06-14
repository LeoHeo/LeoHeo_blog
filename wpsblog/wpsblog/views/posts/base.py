from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from wpsblog.models import Post


class PostBaseView(LoginRequiredMixin, View):
    model = Post
    fields = ["title", "content", "image"]
