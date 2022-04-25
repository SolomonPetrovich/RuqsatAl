from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
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
    new_movies = Movie.objects.all().order_by('-release_date')[:6]

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


def logout_user(request):
    logout(request)
    return redirect('login')


class MovieView(ListView):
    model = Movie
    template_name = 'main/movies.html'
    genres = Genres.objects.all()
    Adventure = Movie.objects.filter(genres__movie__genres='12')[:4]
    Fantasy = Movie.objects.filter(genres__movie__genres='14')[:4]
    Animation = Movie.objects.filter(genres__movie__genres='16')[:4]
    Drama = Movie.objects.filter(genres__movie__genres='18')[:4]
    Horror = Movie.objects.filter(genres__movie__genres='27')[:4]
    Action = Movie.objects.filter(genres__movie__genres='28')[:4]
    Comedy = Movie.objects.filter(genres__movie__genres='35')[:4]
    History = Movie.objects.filter(genres__movie__genres='36')[:4]
    Western = Movie.objects.filter(genres__movie__genres='37')[:4]
    Thriller = Movie.objects.filter(genres__movie__genres='53')[:4]
    Crime = Movie.objects.filter(genres__movie__genres='80')[:4]
    Documentary = Movie.objects.filter(genres__movie__genres='99')[:4]
    Science = Movie.objects.filter(genres__movie__genres='878')[:4]
    Mystery = Movie.objects.filter(genres__movie__genres='9648')[:4]
    Music = Movie.objects.filter(genres__movie__genres='10402')[:4]
    Romance = Movie.objects.filter(genres__movie__genres='10749')[:4]
    Family = Movie.objects.filter(genres__movie__genres='10751')[:4]
    War = Movie.objects.filter(genres__movie__genres='10752')[:4]
    TV = Movie.objects.filter(genres__movie__genres='10770')[:4]
    movie_list = [Adventure, Fantasy, Animation, Drama, Horror, Action, Comedy, History, Western, Thriller, Crime, Documentary, Science, Mystery, Music, Romance, Family, War,TV]

    def get_context_data(self, genres=genres, movie_list=movie_list, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movies'
        context['genres'] = genres
        context['movie_list'] = movie_list
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


def e_ticket(request):
    return render(request, 'main/e-ticket.html')


def profile(request):
    return render(request, 'main/profile.html')


def ticket_booking(request):
    return render(request, 'main/ticket-booking.html')


def seat_seat(request):
    return render(request, 'main/seat_sel.html')
