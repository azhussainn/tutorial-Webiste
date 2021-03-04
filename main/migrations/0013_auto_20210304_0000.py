# Generated by Django 3.1.7 on 2021-03-03 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210303_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialseries',
            name='tutorial_category',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_series',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_slug',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 0, 0, 50, 249723), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='TutorialCategory',
        ),
        migrations.DeleteModel(
            name='TutorialSeries',
        ),
    ]
