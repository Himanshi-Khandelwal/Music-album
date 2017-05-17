from django.conf.urls import url
from django.contrib import admin

from .views import (
	index,
    detail,
	favorite
	)

app_name= 'music'

urlpatterns = [
	url(r'^$', index , name='index'),

	url(r'^music/(?P<album_id>[0-9]+)/$' , detail , name='detail'),
	url(r'^music/(?P<album_id>[0-9]+)/favorite/$' , favorite , name='favorite'),

    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
