# Generated by Django 2.2.2 on 2019-09-05 19:10

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_userrating_priority'),
    ]

    operations = [
        migrations.RenameModel("UserRating", "UserSong")
    ]