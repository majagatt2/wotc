# Generated by Django 4.0.6 on 2023-01-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_alter_registration_day_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='imagen',
            field=models.ImageField(default='tournament imagen', upload_to='tournament/imagen', verbose_name='tournament imagen'),
        ),
    ]