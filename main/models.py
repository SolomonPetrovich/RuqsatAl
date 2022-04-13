from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    ticket_id = models.IntegerField()
    customer = models.ForeignKey('Customer', models.DO_NOTHING, )

    class Meta:
        db_table = 'Booking'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField()

    class Meta:
        db_table = 'Category'


class CreditCard(models.Model):
    credit_card = models.ForeignKey('Payment', models.DO_NOTHING, db_column='credit_card', )
    owner_name = models.CharField()
    experitation_date = models.DateField()
    verification_code = models.IntegerField()

    class Meta:
        db_table = 'Credit_Card'


class User(AbstractUser):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField()
    customer_surname = models.CharField()
    customer_age = models.IntegerField()
    customer_email = models.EmailField()
    customer_phone_number = models.CharField()

    class Meta:
        db_table = 'Customer'


class Favorites(models.Model):
    favorites_id = models.AutoField(primary_key=True)
    movie_id = models.IntegerField()

    class Meta:
        db_table = 'Favorites'


class Hall(models.Model):
    hall = models.ForeignKey('HallSeat', models.DO_NOTHING, )
    hall_name = models.CharField()

    class Meta:
        db_table = 'Hall'


class HallSeat(models.Model):
    hall_seat_id = models.AutoField(primary_key=True)
    seat_id = models.IntegerField()
    hall_id = models.IntegerField()

    class Meta:
        db_table = 'Hall_Seat'


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Favorites, models.DO_NOTHING)
    movie_title = models.CharField()
    movie_year = models.IntegerField()
    movie_runtime = models.IntegerField()
    movie_genres = models.CharField()
    movie_director = models.CharField()
    movie_actors = models.CharField()
    movie_plot = models.TextField()
    movie_posterurl = models.CharField(db_column='movie_posterUrl', )  # Field name made lowercase.

    class Meta:
        db_table = 'Movie'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking_id = models.IntegerField()
    credit_card = models.IntegerField()

    class Meta:
        db_table = 'Payment'


class Seat(models.Model):
    seat = models.ForeignKey(HallSeat, models.DO_NOTHING, )
    amount_of_seats = models.IntegerField()

    class Meta:
        db_table = 'Seat'


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(Booking, models.DO_NOTHING, )
    ticket_price = models.IntegerField()
    number_of_tickets = models.IntegerField()
    ticket_time = models.TimeField()
    ticket_date = models.DateField()
    hall_seats_id = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING, )
    movie = models.ForeignKey(Movie, models.DO_NOTHING, )

    class Meta:
        db_table = 'Ticket'