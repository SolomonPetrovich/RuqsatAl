# Generated by Django 4.0.3 on 2022-05-13 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_booking_booked_datetime_booking_is_paied_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='price',
        ),
    ]
