# Generated by Django 4.0.6 on 2023-01-11 17:13

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('zip', models.IntegerField(null=True)),
                ('phone', models.CharField(max_length=40)),
                ('birthdate', models.DateField(default=datetime.date.today)),
                ('ntrp_rating', models.CharField(blank=True, max_length=10, null=True, verbose_name='NTRP Rating')),
                ('profilePicture', models.ImageField(default='Profile  Picture', upload_to='media/profilePicture')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
                'ordering': ['last_name', 'first_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='Elegir', max_length=50, null=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Relation',
                'verbose_name_plural': 'Relations',
            },
        ),
        migrations.CreateModel(
            name='FamilyMemberRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships', to=settings.AUTH_USER_MODEL)),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reverse_relationships', to=settings.AUTH_USER_MODEL)),
                ('relation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.relations', verbose_name='Select relation:')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='family_members',
            field=models.ManyToManyField(through='users.FamilyMemberRelationship', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.gender', verbose_name='Select gender'),
        ),
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='person',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]