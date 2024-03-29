# Generated by Django 5.0 on 2023-12-26 13:14

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("geo", "0002_alter_city_id_alter_country_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ride",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(max_length=45)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("start_date", models.DateField(null=True)),
                ("end_date", models.DateField(null=True)),
                ("points", models.TextField()),
                ("distance", models.FloatField()),
                ("description", models.CharField(blank=True, max_length=1000)),
                ("is_hide", models.BooleanField(default=False)),
                (
                    "city",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rides",
                        to="geo.city",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="his_rides",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="RideMembers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "ride",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="rides.ride"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ("-id",),
                "unique_together": {("ride", "user")},
            },
        ),
        migrations.AddField(
            model_name="ride",
            name="members",
            field=models.ManyToManyField(
                related_name="members", through="rides.RideMembers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="UserFavorites",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "ride",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="rides.ride"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ("-id",),
                "unique_together": {("ride", "user")},
            },
        ),
        migrations.AddField(
            model_name="ride",
            name="favorites",
            field=models.ManyToManyField(
                related_name="favorites", through="rides.UserFavorites", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
