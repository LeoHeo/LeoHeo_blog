from django.contrib import admin

from wpsblog.models import Post, Comment, NaverPost
from bitly.models import BitLink, BitLinkLog

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(NaverPost)
admin.site.register(BitLink)
admin.site.register(BitLinkLog)
