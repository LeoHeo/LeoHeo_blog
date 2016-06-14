from django.conf.urls import url

from wpsblog.views.posts.comments import *

urlpatterns = [
    url(r'^create/(?P<post_id>\d+)/$', PostCommentCreateView.as_view(), name="create"),
    url(r'^delete/(?P<post_id>\d+)/(?P<comment_id>\d+)/$', comment_delete, name="comment-delete"),
    url(r'^edit/(?P<post_id>\d+)/(?P<comment_id>\d+)/$', comment_edit, name="comment-edit"),
    url(r'^update/(?P<post_id>\d+)/(?P<comment_id>\d+)/$', comment_update, name="comment-update"),
]
