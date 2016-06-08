from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from wpsblog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name="home"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),
    url(r'^about/us/$', about, name="about"),

    url(r'^policy/', include("wpsblog.urls.policy", namespace="policy")),
    url(r'^posts/', include("wpsblog.urls.post", namespace="post")),
    url(r'^naver/posts/$', naver_blog_crawler, name="naver-blog-crawler"),
    url(r'^comments/', include("wpsblog.urls.comments", namespace="comment")),
    url(r'^auth/', include("wpsblog.urls.auth", namespace="auth")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
