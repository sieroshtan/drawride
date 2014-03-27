# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='favorites',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, through='rides.UserFavorites'),
            preserve_default=True,
        ),
    ]
