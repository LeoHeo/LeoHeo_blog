from django.views.generic import DetailView

from wpsblog.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
