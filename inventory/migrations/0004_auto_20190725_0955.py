# Generated by Django 2.2.2 on 2019-07-25 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20190723_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Album'),
        ),
    ]
