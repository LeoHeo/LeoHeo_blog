from django.shortcuts import redirect

from wpsblog.models import Post


def comment_create(request, post_id):
    post = Post.objects.get(id=post_id)

    comment = post.comment_set.create(
        content=request.POST.get('content'),
    )

    return redirect(comment)
