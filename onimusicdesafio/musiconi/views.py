from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm
from django.http import HttpResponse

def home(request):
    songs = Song.objects.all()
    total_songs = songs.count()
    context = {'songs':songs}
    return render(request, 'musiconi/home.html', context)


def createSong(request):
    form = SongForm()
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'musiconi/song_form.html', context)

def updateSong(request, pk):
    
    song = Song.objects.get(id=pk)
    form = SongForm(instance=song)
    
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'musiconi/song_form.html', context)

def deleteSong(request,pk):
    song = Song.objects.get(id=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('/')
    context = {'item':song}
    return render(request,'musiconi/delete.html', context)