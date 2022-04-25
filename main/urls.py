from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('e_ticket/', e_ticket, name='e_ticket'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('ticket_booking/', ticket_booking, name='ticket_booking'),
    path('seat_seal/', seat_seat, name='seat_seal'),
    path('movies/', MovieView.as_view(), name='movies'),
    path('genre/<int:pk>', show_genre, name='movies_genre'),
    path('movie/', show_movie, name='movie'),
    path('profile/', profile, name='profile')
]