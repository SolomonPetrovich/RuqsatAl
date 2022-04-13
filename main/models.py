from django.contrib.auth.models import AbstractUser
from django.db import models


class Hall(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Hall'


class Seat(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Seat'


class HallSeat(models.Model):
    seat = models.ForeignKey('Seat', models.DO_NOTHING)
    hall = models.ForeignKey('Hall', models.DO_NOTHING)

    def __str__(self):
        return self.hall + ' : ' + self.seat

    class Meta:
        db_table = 'Hall_Seat'


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'


class Movie(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    runtime = models.IntegerField()
    genres = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    actors = models.CharField(max_length=150)
    plot = models.TextField()
    poster_url = models.CharField(db_column='posterUrl', max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Movie'


class User(AbstractUser):
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING)

    def __str__(self):
        return self.username


class Favorites(models.Model):
    movie = models.ForeignKey('Movie', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        db_table = 'Favorites'


class Session(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    category = models.ForeignKey('Category', models.DO_NOTHING)
    movie = models.ForeignKey('Movie', models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Session'


class Ticket(models.Model):
    price = models.CharField(max_length=150)
    hall_seats = models.ForeignKey('HallSeat', models.DO_NOTHING)
    movie = models.ForeignKey('Movie', models.DO_NOTHING)
    session = models.ForeignKey('Session', models.DO_NOTHING)

    class Meta:
        db_table = 'Ticket'
