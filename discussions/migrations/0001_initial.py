# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('text', models.TextField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('from_user_deleted', models.BooleanField(default=False)),
                ('to_user_deleted', models.BooleanField(default=False)),
                ('readed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
    ]
