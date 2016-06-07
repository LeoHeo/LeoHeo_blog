from django.conf.urls import url

from wpsblog.views.posts.comments import *

urlpatterns = [
    url(r'^create/(?P<post_id>\d+)/$', comment_create, name="comment_create"),
]
