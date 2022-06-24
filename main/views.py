import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .utils import embed_QR


class HomeView(ListView):
    model = Movie
    template_name = 'main/index.html'
    genres = Genres.objects.all()
    popular_movies = Movie.objects.all().order_by('vote_average')[:4]
    new_movies = Movie.objects.all().order_by('-release_date')[:19]

    def get_context_data(self, genres=genres, popular_movies=popular_movies,
                         new_movies=new_movies, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['genres'] = genres
        context['new_movies'] = new_movies
        context['popular_movies'] = popular_movies
        return context


class MovieView(ListView):
    model = Movie
    template_name = 'main/movies.html'
    genres = Genres.objects.all()
    recent = Movie.objects.all().order_by('-release_date')[:6]
    popular = Movie.objects.all().order_by('-vote_average')[:6]
    Trend = Movie.objects.all().order_by('-popularity')[:6]
    paginate_by = 12

    def get_context_data(self, genres=genres, recent=recent, popular=popular, trend=Trend, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_anonymous:
            favs = Favorites.objects.all()
        else:
            favs = Favorites.objects.filter(
                user=self.request.user).values_list('movie__title', flat=True)
        context['title'] = 'Movies'
        context['genres'] = genres
        context['recent'] = recent
        context['popular'] = popular
        context['trend'] = trend
        context['favs'] = favs
        return context


def search_movie_by_genre(request, pk):
    genre = Genres.objects.get(pk=pk)
    movies = Movie.objects.all()
    genres = Genres.objects.all()
    context = {
        'title': genre,
        'movies': movies,
        'genres': genres
    }
    return render(request, 'main/movie_genre.html', context)


def search_movie_by_name(request):
    genres = Genres.objects.all()
    title = request.GET.get('search')
    movies = Movie.objects.filter(title__contains=title)
    context = {
        'title': 'Searching: ' + title,
        'movies': movies,
        'genres': genres
    }
    return render(request, 'main/movie_search.html', context)


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = Comment.objects.filter(movie=movie)
    genres = Genres.objects.all()
    movie_genres = movie.genres.values()

    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        message = request.POST.get('comment')

        comment = Comment.objects.create(user=user, movie=movie, message=message)
        if comment.save():
            return redirect('movie_detail', id)

    context = {
        'title': movie.title,
        'movie': movie,
        'movie_genres': movie_genres,
        'genres': genres,
        'comments': comments
    }

    return render(request, 'main/movie_detail.html', context)


def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')

        data = {
            'fname': fname,
            'lname': lname,
            'email': email,
            'subject': subject,
            'msg': msg
        }
        message = f'''
        New message:{data['msg']}
        From : {data['email']}
        '''
        send_mail(subject, message, '', ['solizholdasbai@gmail.com'])

    context = {
        'title': 'Contact Us'
    }
    return render(request, 'main/contact.html', context)


def about(request):
    movies = Movie.objects.count()
    admins = User.objects.filter(is_staff=True).count()
    users = User.objects.all().count()
    context = {'title': 'About',
               'movie_count': movies,
               'staff_count': admins,
               'users': users}
    return render(request, 'main/about.html', context)


@login_required(login_url='login')
def addToFavorites(request, id):
    movie = Movie.objects.get(id=id)
    user = User.objects.get(id=request.user.id)
    if not Favorites.objects.all().filter(user=user, movie=movie):
        try:
            Favorites.objects.create(user=user, movie=movie)
        except:
            return redirect('home')
    else:
        try:
            m = Favorites.objects.all().filter(user=user, movie=movie)
            m.delete()
        except:
            return redirect('home')
    return redirect('movies')


@login_required
def profile(request):
    favs = Favorites.objects.all().filter(user=request.user)
    tickets = Booking.objects.all().filter(user=request.user)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user = User.objects.get(id=request.user.id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.phone = phone
        print(user.last_name)
        if user.save():
            messages.error(request, 'Updated Successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'PLease try again')

    context = {'title': 'Profile',
               'favs': favs,
               'tickets': tickets
               }
    return render(request, 'main/profile.html', context)


@login_required
def booking(request, pk):
    sessions = Session.objects.filter(movie_id=pk).values()
    dates = sessions.values_list('date', flat=True).distinct('date')

    context = {
        'title': 'Booking',
        'sessions': sessions,
        'dates': dates
    }

    return render(request, 'main/booking.html', context)


@login_required
def select_seat(request, pk):
    session = Session.objects.get(pk=pk)
    context = {
        'title': 'Seat Selection',
        'session': session
    }
    return render(request, 'main/select_seat.html', context)


@login_required
def seat_seal(request, pk):
    session = Session.objects.get(pk=pk)
    sold_seats = Booking.objects.filter(session__pk=pk).values_list('seat', flat=True)
    s = list(sold_seats)
    ssss = Seat.objects.filter(id__in=s)

    context = {
        'title': 'Booking',
        'sold_seats': ssss,
        'session': session
    }

    return render(request, 'main/seat_sel.html', context)


@login_required
def to_pay(request):
    if request.method == 'POST':
        ids = []
        seats_selected = request.POST['seats'].split(',')
        seats = Seat.objects.all()
        for i in seats_selected:
            ids.append(
                seats.get(row=int(i[:i.find('_')]), number=int(i[i.find('_') + 1:])))
        user = User.objects.get(id=request.user.id)
        session = Session.objects.get(id=int(request.POST['session_id']))
        b = Booking.objects.create(
            user=user, session=session, is_paied=True, booked_datetime=datetime.datetime.now())
        b.seat.set(ids)
        embed_QR(str(b.pk))
        b.qr_code = f'{b.pk}.png'
        b.save()
        return JsonResponse(data={'ans': 'success'})
