import requests
import json

from django.http.response import HttpResponse


def home(request):
    return HttpResponse("hello world")


def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids="
    response = requests.get(url + room_id)
    return HttpResponse(
            response.content,
            content_type = "application/json"
    )


def movies(request, page, per):
    url = "https://watcha.net/home/trailers.json?page={page}&per={per}".format(page = page, per = per)

    response = requests.get(url)
    origin_movies_list = json.loads(response.text)["trailers"]
    select_elements_list = []

    for movie in origin_movies_list:
        select = "<p>title : {title}</p>".format(title = movie['title'])
        select += "\n<p>rate : {rate}</p>".format(rate = movie['filmrate'])
        select += "\n<p>genre : {genre}</p>".format(genre = movie['main_genre'])
        select += "\n<p>story : {story}</p>".format(story = movie.get('short_story', '') or '')
        select += "<img src='{src}' width=150 height=200  />".format(src = movie['poster']['url'])
        
        select_elements_list.append(select)


    return HttpResponse("\n".join(select_elements_list))
