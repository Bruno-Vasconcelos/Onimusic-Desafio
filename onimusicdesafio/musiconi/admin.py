from django.contrib import admin

# Register your models here.
from .models import Song

@admin.register(Song)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "artist")