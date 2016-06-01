from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_blog_crawler(request):
    keyword = request.GET.get('keyword')
    query = request.GET.get('query')

    post_list = NaverPost.objects.all()

    if keyword:
        post_list = post_list.filter(keyword=keyword)

    if query:
        post_list = post_list.filter(title__contains=query)

    return render(
        request,
        "naver_post/list.html",
        {
            "keyword": keyword,
            "query": query,
            "post_list": post_list
        }
    )
