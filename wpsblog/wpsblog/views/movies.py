import requests
import json

from django.http.response import HttpResponse


def movies(request, category, page, per):
    url = "https://watcha.net/home/{category}.json?page={page}&per={per}".format(
            category=category,
            page=page,
            per=per,
    )

    response = requests.get(url)
    origin_movies_list = json.loads(response.text)[category]
    select_elements_list = []

    select_elements_list.append("Total data: {total}".format(total=len(origin_movies_list)))

    for movie in origin_movies_list:
        select = "<p>title : {title}</p>".format(title=movie.get('title'))

        if category == "trailers":
            select += "\n<p>rate : {rate}</p>".format(rate=movie.get('filmrate'))
            select += "\n<p>genre : {genre}</p>".format(genre=movie.get('main_genre'))
            select += "\n<p>story : {story}</p>".format(story=movie.get('short_story', '') or '')
            select += "<img src='{src}' width=150 height=200  />".format(src=movie['poster']['url'])
        elif category == "news":
            select += "\n<p>{content}</p>".format(content=movie.get('content'))
            select += "\n<img src='{src}' width=150 height=200>".format(src=movie.get('image'))

        select_elements_list.append(select)

    return HttpResponse("\n".join(select_elements_list))
