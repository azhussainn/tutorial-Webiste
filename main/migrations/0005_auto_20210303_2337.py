# Generated by Django 3.1.7 on 2021-03-03 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210303_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 23, 37, 39, 812192), verbose_name='date published'),
        ),
    ]
