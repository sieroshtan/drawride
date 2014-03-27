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
            name='Follow',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('follower', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('followee', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'unique_together': set([('follower', 'followee')]),
            },
            bases=(models.Model,),
        ),
    ]
