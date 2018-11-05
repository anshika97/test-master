from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.staticfiles.templatetags.staticfiles import static

from .models import Movie, Person

from .forms import MovieForm, PersonForm

# Create your views here.

def index(request):
    movies_list = Movie.objects.all()
    return render(request, 'movie/index.html',{
        'movies_list': movies_list,
    })

def new_movie(request):
    if request.method == 'POST':

        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            movie = Movie(
                title=form.cleaned_data['title'],
                cover_photo=form.cleaned_data['cover_photo'],
                description=form.cleaned_data['description'],
                release_date=form.cleaned_data['release_date'],
                rating=form.cleaned_data['rating'],
            )

            movie.save()

            return redirect('movie:index')
    else:
        form = MovieForm()

    return render(request, 'movie/new_movie.html',{
        'form': form,
    })

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    directors = movie.directors.all()
    writers = movie.writers.all()
    actors = movie.actors.all()
    return render(request, 'movie/movie_detail.html', {
        'movie': movie,
        'directors': directors,
        'writers': writers,
        'actors': actors,
        'rating_img_url': static('movie/images/rating{}.png'.format(movie.rating))
    })


def edit_movie_staff(request, movie_id, staff_type):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)

        if form.is_valid():
            person = Person(
                name=form.cleaned_data['name'],
                photo=form.cleaned_data['photo'],
                bio=form.cleaned_data['bio'],
                dob=form.cleaned_data['dob'],
            )

            person.save()

            movie.add_staff(staff_type, person)

            return redirect('movie:movie_detail', movie_id=movie.id)
    else:
        form = PersonForm()

    return render(request, 'movie/edit_staff.html',{
        'form': form,
        'movie': movie,
    })
