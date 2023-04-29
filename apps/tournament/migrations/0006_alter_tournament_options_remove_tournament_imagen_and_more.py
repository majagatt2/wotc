# Generated by Django 4.0.6 on 2023-02-25 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0005_tournament_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'ordering': ['date'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='imagen',
        ),
        migrations.AddField(
            model_name='tournament',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Tournament'),
        ),
    ]
