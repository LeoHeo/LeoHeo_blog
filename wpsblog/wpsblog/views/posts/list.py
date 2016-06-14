from django.views.generic import ListView
from django.core.paginator import Paginator

from wpsblog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_paginate_by(self, queryset):
        return self.request.GET.get("per", 5)
