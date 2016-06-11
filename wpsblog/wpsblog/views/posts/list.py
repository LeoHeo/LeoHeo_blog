import math

from django.shortcuts import render
from wpsblog.models import Post


def list(request):
    page = int(request.GET.get('page') or 1)
    per = int(request.GET.get('per') or 5)
    pagination = math.ceil(Post.objects.public().count() / per)

    start = (page * per) - per
    end = (page * per)

    return render(
        request,
        "posts/list.html",
        {
            "posts_list": Post.objects.public()[start:end],
            "page_list": range(1, pagination+1),
            "per": per,
        }
    )
