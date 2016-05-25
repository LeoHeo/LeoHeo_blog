import requests
import json

from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import render


def home(request):
    return render(
        request,
        "home.html",
        {"site_name": "wps blog"}
    )
    

def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids="
    response = requests.get(url + room_id)
    return HttpResponse(
            response.content,
            content_type = "application/json"
    )


def movies(request, category, page, per):
    url = "https://watcha.net/home/{category}.json?page={page}&per={per}".format(
            category = category,
            page = page, 
            per = per)

    response = requests.get(url)
    origin_movies_list = json.loads(response.text)[category]
    select_elements_list = []

    select_elements_list.append("Total data: {total}".format(total = len(origin_movies_list)))
            
    for movie in origin_movies_list:
        select = "<p>title : {title}</p>".format(title = movie.get('title'))
        

        if category == "trailers":
            select += "\n<p>rate : {rate}</p>".format(rate = movie.get('filmrate'))
            select += "\n<p>genre : {genre}</p>".format(genre = movie.get('main_genre'))
            select += "\n<p>story : {story}</p>".format(story = movie.get('short_story', '') or '')
            select += "<img src='{src}' width=150 height=200  />".format(src = movie['poster']['url'])
        
        elif category == "news":
            select += "\n<p>{content}</p>".format(content = movie.get('content'))
            select += "\n<img src='{src}' width=150 height=200>".format(src = movie.get('image'))


        select_elements_list.append(select)
    
    return HttpResponse("\n".join(select_elements_list))


def search(request):
    search = request.GET.get('search')
    url = "https://watcha.net/home/news.json?page=1&per=12"
    
    template = loader.get_template("news.html")

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



