from django.http.response import HttpResponse
import requests

def home(request):
    return HttpResponse("hello world")

def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids="
    response = requests.get(url + room_id)
    return HttpResponse(
            response.content,
            content_type = "application/json"
    )


