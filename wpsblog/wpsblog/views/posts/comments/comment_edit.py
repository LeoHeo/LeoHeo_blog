from django.shortcuts import render

from wpsblog.models import Post


def comment_edit(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    return render(
        request,
        "posts/detail.html",
        {
            "post": post,
            "comment": comment,
        }
    )
