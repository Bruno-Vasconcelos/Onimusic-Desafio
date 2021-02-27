from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm

class SongListView(ListView):
    model = Song


def createSong(request):
    form = SongForm()
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'musiconi/song_form.html', context)
