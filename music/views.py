from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Album ,Songs

def index(request):
    all_albums= Album.objects.all()
    context={
        'all_albums' : all_albums,
    }

    return render(request,"index.html",context)

def detail(request,album_id):
    # try:
    #      album=Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #      raise Http404("Album doesnot exist")
    album=get_object_or_404(Album,id=album_id)
    context={
        'album' : album ,
    }
    return render(request,"detail.html",context)


def favorite(request , album_id):
    album=get_object_or_404(Album,id=album_id)
    context={
        'album' : album ,
        'error_message' : "You didnot select a valid song"
    }
    try :
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError , Song.DoesNotExist):
        return render(request,"detail.html",context)
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,"detail.html",context)
