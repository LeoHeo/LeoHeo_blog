from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from .base import PostBaseView


class PostCreateView(PostBaseView, CreateView):
    template_name = "posts/new.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
