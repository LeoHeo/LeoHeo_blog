from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from wpsblog.models import Comment


class CommentBaseView(LoginRequiredMixin, View):
    model = Comment
    fields = ["content"]
