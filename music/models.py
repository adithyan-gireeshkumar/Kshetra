from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='artists/',
         blank=True,
          null=True)

    def __str__(self):
        return self.name
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, 
    on_delete =models.CASCADE, related_name="albums")
    cover=models.ImageField(
        upload_to='albums/',
        blank=True,
        null=True
    )
    release_date=models.DateField(blank=True, null=True)
    def __str__(self):
        return self.title
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="songs"
    )        
    album = models.ForeignKey(
        Album ,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="songs"
    )
    audio_file = models.FileField(
        upload_to='songs/'
    )
    cover = models.ImageField(
        upload_to='songs/covers/',
        blank=True,
        null=True,
    )
    language = models.CharField(
        max_length=100,
        blank=True,
        
    )
    deity = models.CharField(
        max_length=100,
        blank=True,
    )
    duration = models.PositiveIntegerField(
        default=0,
        help_text="Duration in seconds"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Lyrics(models.Model):
    song = models.OneToOneField(
        Song,
        on_delete=models.CASCADE,
        related_name="lyrics"
    )
    text = models.TextField()
    def __str__(self):
        return f"Lyrics for {self.song.title}"        