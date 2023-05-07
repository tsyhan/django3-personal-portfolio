# Generated by Django 4.1.7 on 2023-04-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(max_length=250)),
                ("date", models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name="Project",
        ),
    ]