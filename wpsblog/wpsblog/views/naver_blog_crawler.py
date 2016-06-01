from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_blog_crawler(request):
    keyword = request.GET.get('keyword')
    post_list = NaverPost.objects.all()

    if keyword:
        post_list = [
            post
            for post
            in post_list
            if post.keyword == keyword
        ]

    return render(
        request,
        "naver_post/list.html",
        {
            "keyword": keyword,
            "post_list": post_list
        }
    )
