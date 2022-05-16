from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('movies/', MovieView.as_view(), name='movies'),
    path('genre/<int:pk>', show_genre, name='movies_genre'),
    path('movie_detail/<int:pk>', movie_detail, name='movie_detail'),
    path('movie/', show_movie, name='movie'),
    path('profile/', profile, name='profile'),
    path('favorites/<int:id>/', addToFavorites, name='addtofavs'),
    path('booking/<int:pk>', booking, name='booking'),
    path('select_seat/<int:pk>', select_seat, name='select_seat'),
    path('seat_seal/<int:pk>', seat_seal, name='seat_seal'),
    path('select_seat/topay', to_pay, name='topay'),
    path('qr/checking/<int:session_pk>/<int:user_pk>', qr_check, name='check'),
]
