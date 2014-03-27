# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', to_field='id')),
                ('object_id', models.PositiveIntegerField()),
                ('text', models.TextField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
    ]
