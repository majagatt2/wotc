# Generated by Django 4.0.6 on 2023-03-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0005_tournament_list_public_alter_tournament_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='register',
            field=models.BooleanField(default=False, verbose_name='Register on'),
        ),
    ]