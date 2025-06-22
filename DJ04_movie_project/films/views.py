from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'films/add_movie.html', {'form': form})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'films/movie_list.html', {'movies': movies})


from django.shortcuts import render

# Create your views here.
