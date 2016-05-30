from django.http.response import HttpResponse


def room(request, room_id):
    return HttpResponse("room")
