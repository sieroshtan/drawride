# encoding: utf8
from django.db import models, migrations
import users.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__first__'),
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(max_length=45, db_index=True, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(choices=[('n', 'Not specified'), ('m', 'Male'), ('f', 'Female')], max_length=1, default='n')),
                ('bio', models.TextField(blank=True, max_length=1000)),
                ('lang', models.CharField(choices=[('ru', 'Russian'), ('en', 'English')], max_length=2, blank=True)),
                ('photo', models.ImageField(upload_to=users.models.get_file_path)),
                ('city', models.ForeignKey(blank=True, to_field='id', null=True, to='geo.City')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, verbose_name='groups', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, verbose_name='user permissions', to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
