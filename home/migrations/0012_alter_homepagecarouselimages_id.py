# Generated by Django 5.0.9 on 2024-10-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_homepagecarouselimages"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepagecarouselimages",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
