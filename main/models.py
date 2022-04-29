from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class Hall(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hall'
        verbose_name_plural = 'Halls'


class Seat(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Seat'
        verbose_name_plural = 'Seats'


class HallSeat(models.Model):
    seat = models.ForeignKey('Seat', models.DO_NOTHING)
    hall = models.ForeignKey('Hall', models.DO_NOTHING)

    def __str__(self):
        return self.hall + ' : ' + self.seat

    class Meta:
        verbose_name = 'HeallSeat'
        verbose_name_plural = 'HallSeats'


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Genres(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    title = models.CharField(max_length=150)
    original_title = models.CharField(max_length=150)
    original_language = models.CharField(max_length=150)
    overview = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.CharField(null=True, max_length=500)
    release_date = models.DateField(null=True, max_length=150)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genres)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Admin(BaseUserManager):
    pass


class User(AbstractUser):
    phone = models.CharField(null=True, max_length=150)

    def __str__(self):
        return self.username


class Session(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    category = models.ForeignKey('Category', models.DO_NOTHING)
    movie = models.ForeignKey('Movie', models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'


class Ticket(models.Model):
    price = models.CharField(max_length=150)
    hall_seats = models.ForeignKey('HallSeat', models.DO_NOTHING)
    movie = models.ForeignKey('Movie', models.DO_NOTHING)
    session = models.ForeignKey('Session', models.DO_NOTHING)

    def __str__(self):
        return self.session + ' ' + self.movie + ' ' + self.hall_seats + ' ' + self.price

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


class Booking(models.Model):
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    def __str__(self):
        return self.user + ' ' + self.ticket

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'


class Favorites(models.Model):
    movie = models.ForeignKey('Movie', models.CASCADE)
    user = models.ForeignKey('User', models.CASCADE)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return self.user.username + ' ' + self.movie.title