from django.conf.urls import url
from django.contrib import admin

from .views import (
	IndexView,
	DetailView,
	AlbumCreate,
	AlbumUpdate,
	AlbumDelete,
	UserFormView
	)

app_name= 'music'

urlpatterns = [
	url(r'^$', IndexView.as_view() , name='index'),
	url(r'^music/register/$', UserFormView.as_view() , name='register'),
	url(r'^music/(?P<pk>[0-9]+)/$' , DetailView.as_view() , name='detail'),
	url(r'^music/album/add/$', AlbumCreate.as_view() , name='album-add'),
	url(r'^album/(?P<pk>[0-9]+)/$', AlbumUpdate.as_view() , name='album-update'),
	url(r'^album/(?P<pk>[0-9]+)/delete/$', AlbumDelete.as_view() , name='album-delete'),


]
