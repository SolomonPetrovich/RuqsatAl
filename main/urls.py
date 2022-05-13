from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('movies/', MovieView.as_view(), name='movies'),
    path('genre/<int:pk>', show_genre, name='movies_genre'),
    path('movie_detail/<int:pk>', movie_detail, name='movie_detail'),
    path('movie/', show_movie, name='movie'),
    path('profile/', profile, name='profile'),
    path('favorites/<int:id>', addToFavorites, name='addtofavs'),
    path('booking/<int:pk>', booking, name='booking'),
    path('select_seat/<int:pk>', select_seat, name='select_seat'),
    path('seat_seal/<int:pk>', seat_seal, name='seat_seal'),
    path('select_seat/topay', topay, name='topay'),
    path('ticket/<int:session_pk>/', ticket, name='ticket'),
]
