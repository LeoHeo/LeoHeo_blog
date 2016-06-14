from django.conf.urls import url

from bitly.views import *

urlpatterns = [
    url(r'^new/$', BitLinkCreateView.as_view(), name="create"),
    url(r'^(?P<shorten_hash>\w+)/dashboard/$', BitLinkDashBoardView.as_view(), name="dashboard"),
    url(r'^(?P<shorten_hash>\w+)/$', BitLinkRedirectView.as_view(), name="redirect"),
]
