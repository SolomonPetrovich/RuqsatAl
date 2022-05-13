from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Hall(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hall'
        verbose_name_plural = 'Halls'


class Seat(models.Model):
    row = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return str(self.row) + '_' + str(self.number)

    class Meta:
        verbose_name = 'Seat'
        verbose_name_plural = 'Seats'


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
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    hall = models.ForeignKey('Hall', models.CASCADE)
    movie = models.ForeignKey('Movie', models.CASCADE)

    def __str__(self):
        return self.movie.title + ' ' + str(self.date) + ' ' + str(self.time)

    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'


class Booking(models.Model):
    session = models.ForeignKey('Session', models.CASCADE)
    seat = models.ManyToManyField('Seat')
    user = models.ForeignKey('User', models.CASCADE)
    booked_datetime = models.DateTimeField(default=None)
    is_paied = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

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