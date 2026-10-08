from django.contrib import admin

from .models import Artist, Album, Song ,Lyrics

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date')
    search_fields = ('title', 'artist__name')
    list_filter = ('artist',)
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'language', 'deity', 'created_at')
    search_fields = ('title', 'artist__name', 'album__title','deity')
    list_filter = ('language', 'deity','created_at')
@admin.register(Lyrics)
class LyricsAdmin(admin.ModelAdmin):
    list_display = ('song',)
    search_fields = ('song__title',)