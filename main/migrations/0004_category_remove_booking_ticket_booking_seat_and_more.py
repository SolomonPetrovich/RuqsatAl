# Generated by Django 4.0.3 on 2022-05-11 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_ticket_category_ticket_price_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField(default=None)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='booking',
            name='ticket',
        ),
        migrations.AddField(
            model_name='booking',
            name='seat',
            field=models.ManyToManyField(to='main.seat'),
        ),
        migrations.AddField(
            model_name='booking',
            name='session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.session'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
