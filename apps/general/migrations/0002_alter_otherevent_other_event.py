# Generated by Django 4.0.6 on 2023-01-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherevent',
            name='other_event',
            field=models.CharField(max_length=50, verbose_name='Event'),
        ),
    ]
