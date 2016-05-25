"""wpsblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# MVC
# M_Model: DB( Data ) & Business Logic
# V_View: HTML, CSS, ... -> Templates/Client
# C_Controller: View, Model ...

# Model => 더 무겁게
# Controller => 더 가볍게(즉, 기능이 Controller => Model...)

# MVC
# MVVM
# MVW
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

# MVC Controller
from wpsblog.views import home, room, movies, search


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^$', home),
    url(r'^rooms/(?P<room_id>\d+)/$', room),
    url(r'^movies/(?P<category>\w+)/(?P<page>\d+)/(?P<per>\d+)', movies),
    url(r'^search/$', search)
]
