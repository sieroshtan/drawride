# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(null=True, blank=True, max_length=40),
            preserve_default=True,
        ),
    ]
