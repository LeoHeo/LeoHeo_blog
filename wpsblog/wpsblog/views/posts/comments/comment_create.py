from django.views.generic.edit import CreateView

from .comment_base import CommentBaseView
from wpsblog.models import Post


class PostCommentCreateView(CommentBaseView, CreateView):
    template_name = "posts/detail.html"

    def form_valid(self, form):
        post_user = self.request.user
        kwargs = self.kwargs

        form.instance.user = post_user
        form.instance.post = Post.objects.get(
            id=self.kwargs.get("post_id"),
        )
        return super(PostCommentCreateView, self).form_valid(form)
