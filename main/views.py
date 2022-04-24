from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import CustomLoginUserForm, CustomRegisterUserForm
from django.views.generic import *


class HomeView(ListView):
    model = Movie
    template_name = 'main/index.html'
    genres = Genres.objects.all()

    def get_context_data(self, genres=genres,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['genres'] = genres
        return context


class ContactView(View):
    template_name = 'main/Contact_Us.html'


def about(request):
    movies = Movie.objects.count()
    admins = User.objects.filter(is_staff=True).count()
    users = User.objects.all().count()
    context = {'title': 'About',
               'movie_count': movies,
               'staff_count': admins,
               'users': users}
    return render(request, 'main/about.html', context)


def e_ticket(request):
    return render(request, 'main/e-ticket.html')


def profile(request):
    return render(request, 'main/profile.html')


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


def logout_user(request):
    logout(request)
    return redirect('login')


def ticket_booking(request):
    return render(request, 'main/ticket-booking.html')


def seat_seat(request):
    return render(request, 'main/seat_sel.html')


class MovieView(ListView):
    model = Movie
    template_name = 'main/movies.html'
    genres = Genres.objects.all()
    paginate_by = 12
    ordering = ['-popularity']

    def get_context_data(self, genres=genres, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movies'
        context['genres'] = genres
        return context


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
    return render(request, 'main/movie.html', context)


class MovieGenreView(ListView):
    model = Movie
    template_name = 'main/movie_genre.html'
    context_object_name = 'genre'

    def get_queryset(self):
        return Movie.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movies'
        return context