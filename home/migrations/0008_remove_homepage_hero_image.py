# Generated by Django 5.0.9 on 2024-09-20 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_rename_image_homepage_hero_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homepage",
            name="hero_image",
        ),
    ]
