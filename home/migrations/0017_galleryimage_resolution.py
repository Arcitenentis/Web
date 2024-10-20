# Generated by Django 5.0.9 on 2024-10-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_galleryimage_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="galleryimage",
            name="resolution",
            field=models.CharField(
                choices=[
                    ("low", "Low (400x300)"),
                    ("medium", "Medium (800x600)"),
                    ("high", "High (1200x900)"),
                ],
                default="medium",
                max_length=50,
            ),
        ),
    ]
