# Generated by Django 3.2.23 on 2024-05-19 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_auto_20240518_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movie_app.director'),
        ),
    ]
