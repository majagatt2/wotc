# Generated by Django 4.0.6 on 2023-04-10 21:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_newsletter_email_newsletter_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]