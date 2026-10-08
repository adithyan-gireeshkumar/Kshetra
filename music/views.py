from django.shortcuts import render

def home(request):
    songs = Song.objects.select_related("artist", "album").order_by("created_at")[:10]

    albums = Album.objects.select_related("artist").order_by("release_date")[:6]

    artists = Artist.objects.all()[:6]

    context ={

        "songs" : songs,
        "albums" : albums,
        "artists" : artists,
    }

    return render(request, "music/home.html", context)
