from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import *
from django.core.mail import send_mail


class HomeView(ListView):
    model = Movie
    template_name = 'main/index.html'
    genres = Genres.objects.all()
    header_movies = Movie.objects.all().order_by('vote_average')[:4]
    popular_movies = Movie.objects.all().order_by('vote_average')[:4]
    new_movies = Movie.objects.all().order_by('-release_date')[:19]

    def get_context_data(self, genres=genres, header_movies=header_movies, popular_movies=popular_movies, new_movies=new_movies,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['genres'] = genres
        context['new_movies'] = new_movies
        context['header_movies'] = header_movies
        context['popular_movies'] = popular_movies
        return context


class RegisterView(CreateView):
    form_class = CustomRegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUserView(LoginView):
    form_class = CustomLoginUserForm
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Log in'
        return context


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


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
            favs = Favorites.objects.filter(user=self.request.user).values_list('movie__title', flat=True)
        context['title'] = 'Movies'
        context['genres'] = genres
        context['recent'] = recent
        context['popular'] = popular
        context['trend'] = trend
        context['favs'] = favs
        return context


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {'title': movie.title,
               'movie': movie}
    return render(request, 'main/movie_detail.html', context)


def show_genre(request, pk):
    genre = Genres.objects.get(pk=pk)
    movies = Movie.objects.all()
    genres = Genres.objects.all()
    context = {'title': genre,
               'movies': movies,
               'genres': genres}
    return render(request, 'main/movie_genre.html', context)


def show_movie(request):
    title = request.GET.get('search')
    movies = Movie.objects.filter(title__contains=title)
    context = {'title': 'Searching: ' + title,
               'movies': movies}
    return render(request, 'main/movie_search.html', context)


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
        print(data)
        message = f'''
        New message:{data['msg']}
        From : {data['email']}
        '''
        send_mail(subject, message, '', ['solizholdasbai@gmail.com'])

    context = {'title': 'Contact Us'}
    return render(request, 'main/Contact_Us.html', context)


def about(request):
    movies = Movie.objects.count()
    admins = User.objects.filter(is_staff=True).count()
    users = User.objects.all().count()
    context = {'title': 'About',
               'movie_count': movies,
               'staff_count': admins,
               'users': users}
    return render(request, 'main/about.html', context)


@login_required
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


def e_ticket(request):
    return render(request, 'main/e-ticket.html')


@login_required
def profile(request):
    favs = Favorites.objects.all().filter(user=request.user)
    context = {'title': request.user.username,
               'favs' : favs}
    return render(request, 'main/profile.html', context)


def ticket_booking(request, pk):
    movie = Movie.objects.get(pk=pk)
    seat = 'main/seat_seal.html'
    context = {'title': 'Booking',
               'movie_id': movie.id,
               'seat': seat}
    return render(request, 'main/ticket-booking.html', context)


def seat_seat(request):
    return render(request, 'main/seat_sel.html')
