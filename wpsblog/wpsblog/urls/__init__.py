from django.conf.urls import url, include
from django.contrib import admin

from wpsblog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name="home"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),
    url(r'^about/us/$', about, name="about"),

    url(r'^policy/', include("wpsblog.urls.policy", namespace="policy"))
]

# 1. policy_urlpatterns 변수로
# 2. policy_urlpatterns를 파일로 (from .. import ..)
# 3. policy_urls라는 모듈로 (include 가 모듈이름을 받을 수 있었다.)
