# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0002_ride_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='rides.RideMembers'),
            preserve_default=True,
        ),
    ]
