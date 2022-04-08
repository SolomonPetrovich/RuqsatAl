from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('e_ticket/', views.e_ticket, name='e_ticket'),
    path('signin/', views.sign_in, name='sign_in'),
    path('ticket_booking/', views.ticket_booking, name='ticket_booking'),
    path('seat_seal/', views.seat_seat, name='seat_seal'),
    path('movies/', views.movies, name='movies'),
]