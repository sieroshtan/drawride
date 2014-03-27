# encoding: utf8
from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('title', models.CharField(max_length=45)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('points', models.TextField()),
                ('distance', models.FloatField()),
                ('description', models.CharField(max_length=1000, blank=True)),
                ('city', models.ForeignKey(default=0, to='geo.City', to_field='id')),
                ('is_hide', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RideMembers',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('ride', models.ForeignKey(to='rides.Ride', to_field='id')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'unique_together': set([('ride', 'user')]),
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFavorites',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('ride', models.ForeignKey(to='rides.Ride', to_field='id')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'unique_together': set([('ride', 'user')]),
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
    ]
