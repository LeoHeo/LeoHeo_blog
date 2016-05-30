import requests
import json

from django.shortcuts import render

def news(request):
    search = request.GET.get('search')
    url = "https://watcha.net/home/news.json?page=1&per=12"
    
    response = requests.get(url)
    news_list = json.loads(response.text).get('news')

    if search:
        news_list = list(filter(
            lambda news: search in news.get('title'),
            news_list,
        ))
   
    return render(
        request,
        "news.html",
        {"news_list":news_list}
    )
