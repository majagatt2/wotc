# Generated by Django 4.0.6 on 2023-04-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_person_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], max_length=10)),
                ('email', models.ManyToManyField(to='users.newsletteruser')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]