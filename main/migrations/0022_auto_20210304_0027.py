# Generated by Django 3.1.7 on 2021-03-03 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210304_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 0, 27, 54, 900045), verbose_name='date published'),
        ),
    ]
