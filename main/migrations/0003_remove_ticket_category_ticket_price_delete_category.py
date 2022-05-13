# Generated by Django 4.0.3 on 2022-05-11 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_ticket_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='category',
        ),
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
