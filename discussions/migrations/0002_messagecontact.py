# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageContact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('latest_message', models.ForeignKey(to='discussions.Message', to_field='id')),
                ('from_user_deleted', models.BooleanField(default=False)),
                ('to_user_deleted', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': set([('from_user', 'to_user')]),
                'ordering': ('-latest_message',),
            },
            bases=(models.Model,),
        ),
    ]
