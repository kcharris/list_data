# Generated by Django 2.2.2 on 2019-07-26 11:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20190726_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='rating',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
