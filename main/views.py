from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import CustomLoginUserForm, CustomRegisterUserForm
from django.views.generic import *

# Create your views here.


class HomeView(ListView):
    model = Movie
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class ContactView(View):
    template_name = 'main/Contact_Us.html'


def about(request):
    return render(request, 'main/about.html')


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movies'
        return context