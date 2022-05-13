# Generated by Django 4.0.3 on 2022-05-12 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_remove_booking_ticket_booking_seat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_paied',
        ),
        migrations.RemoveField(
            model_name='session',
            name='hall',
        ),
        migrations.AddField(
            model_name='booking',
            name='hall',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.hall'),
            preserve_default=False,
        ),
    ]
