from django.contrib import admin
from .models import Song
from .models import Artist

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "artist")

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "date_joined",)

