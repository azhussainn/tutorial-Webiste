# Generated by Django 3.1.7 on 2021-03-03 18:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210304_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 0, 17, 27, 415983), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.tutorialseries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='tutorial_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tutorialcategory', verbose_name='Category'),
        ),
    ]
