# Generated by Django 3.2.23 on 2024-05-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movie_app.Actor'),
        ),
    ]
