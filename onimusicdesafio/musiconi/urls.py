from django.urls import path
from . import views

app_name = "musiconi"

urlpatterns = [
    path("", views.SongListView.as_view(),name = "list"),
    path('create_song/', views.createSong, name = "create_song"), 
    path('update_song/<str:pk>/', views.updateSong, name = "update_song"),
    path('delete_song/<str:pk>/', views.deleteSong, name = "delete_song"),
]
