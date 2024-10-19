from django import forms
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from colorfield.fields import ColorField

class HomePageCarouselImages(models.Model):
    page = ParentalKey('home.HomePage', related_name='carousel_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('image'),
    ]

    class Meta:
        verbose_name = "Carousel Image"
        verbose_name_plural = "Carousel Images"

class HomePage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Background Image",
        help_text="Image to display as the background"
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_text_color = ColorField(default='#000000', verbose_name="Hero Text Color")
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_color = ColorField(default='#000000', verbose_name="Hero CTA Color")
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )
    head_body = RichTextField(blank=True)
    head_body_color = ColorField(default='#000000', verbose_name="Head Body Color")
    body = RichTextField(blank=True)
    body_color = ColorField(default='#000000', verbose_name="Body Color")

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("background_image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_text_color"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_color"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("head_body"),
                FieldPanel("head_body_color"),
                FieldPanel("body"),
                FieldPanel("body_color"),
            ],
            heading="Content section",
        ),
        InlinePanel('carousel_images', label="Carousel Images"),
    ]

class GalleryImage(models.Model):
    page = ParentalKey('GalleryPage', related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(max_length=255, blank=True)
    size = models.CharField(
        max_length=50,
        choices=[
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large'),
        ],
        default='medium',
    )
    resolution = models.CharField(
        max_length=50,
        choices=[
            ('low', 'Low (400x300)'),
            ('medium', 'Medium (800x600)'),
            ('high', 'High (1200x900)'),
        ],
        default='medium',
    )

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
        FieldPanel('size'),
        FieldPanel('resolution'),
    ]

class GalleryPage(Page):
    intro = RichTextField(blank=True)
    layout = models.CharField(
        max_length=50,
        choices=[
            ('grid', 'Grid'),
            ('masonry', 'Masonry'),
            ('slider', 'Slider'),
        ],
        default='grid',
    )
    image_size = models.CharField(
        max_length=50,
        choices=[
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large'),
        ],
        default='medium',
    )
    image_format = models.CharField(
        max_length=50,
        choices=[
            ('square', 'Square'),
            ('landscape', 'Landscape'),
            ('portrait', 'Portrait'),
        ],
        default='landscape',
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('gallery_images', label="Gallery Images"),
        FieldPanel('layout'),
        FieldPanel('image_size'),
        FieldPanel('image_format'),
    ]

    class Meta:
        verbose_name = "Gallery Page"
        verbose_name_plural = "Gallery Pages"