# Generated by Django 4.2.13 on 2024-07-07 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
        ('genres', '0001_initial'),
        ('movies', '0002_rename_moview_movies'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
