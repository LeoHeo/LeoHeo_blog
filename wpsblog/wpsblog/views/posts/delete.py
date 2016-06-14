from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from .base import PostBaseView


class PostDeleteView(PostBaseView, DeleteView):
    template_name = "posts/list.html"
    success_url = reverse_lazy("post:list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
