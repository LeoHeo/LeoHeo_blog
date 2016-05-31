from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_blog_crawler(request):
    return render(
        request,
        "naver_blog_list.html",
        {"blog_list": NaverPost.objects.all()}
    )
