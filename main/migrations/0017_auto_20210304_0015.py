# Generated by Django 3.1.7 on 2021-03-03 18:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210304_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 0, 15, 49, 973725), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.tutorialseries', verbose_name='Series'),
        ),
    ]
