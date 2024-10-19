# Generated by Django 5.0.9 on 2024-10-19 11:36

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_alter_homepagecarouselimages_id"),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
                (
                    "gallery_images",
                    models.ManyToManyField(blank=True, to="wagtailimages.image"),
                ),
            ],
            options={
                "verbose_name": "Gallery Page",
                "verbose_name_plural": "Gallery Pages",
            },
            bases=("wagtailcore.page",),
        ),
    ]
