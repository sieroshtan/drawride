# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.ForeignKey(to_field='id', to='geo.Country')),
                ('name', models.CharField(max_length=255)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lng', models.FloatField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
