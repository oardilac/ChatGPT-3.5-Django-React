# Generated by Django 4.2.1 on 2023-06-04 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filename", models.CharField(max_length=255)),
                ("location", models.URLField()),
                ("file_type", models.CharField(max_length=50)),
                ("file_size", models.IntegerField()),
                ("file_encoding", models.CharField(max_length=50)),
                ("modification_time", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="TextFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filename", models.CharField(max_length=255)),
                ("location", models.URLField()),
                ("file_type", models.CharField(max_length=50)),
                ("file_size", models.IntegerField()),
                ("file_encoding", models.CharField(max_length=50)),
                ("modification_time", models.DateTimeField(auto_now=True)),
                ("tokens", models.IntegerField()),
                ("characters", models.IntegerField()),
            ],
        ),
    ]