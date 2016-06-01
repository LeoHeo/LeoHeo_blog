from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_blog_crawler(request):
    return render(
        request,
        "naver_post/list.html",
        {"blog_list": NaverPost.objects.all()}
    )
