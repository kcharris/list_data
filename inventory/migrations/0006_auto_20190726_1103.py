# Generated by Django 2.2.2 on 2019-07-26 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20190726_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='rating',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
