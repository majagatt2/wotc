# Generated by Django 4.0.6 on 2023-01-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(default='', max_length=50, verbose_name=''),
        ),
    ]
