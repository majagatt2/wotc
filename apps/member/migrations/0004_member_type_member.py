# Generated by Django 4.0.6 on 2023-01-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_costsmembers_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='type_member',
            field=models.CharField(default='', max_length=50, verbose_name='type'),
        ),
    ]