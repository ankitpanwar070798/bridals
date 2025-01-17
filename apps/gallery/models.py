from django.db import models
from apps.carousel.models import VIDEO_PROVIDER_CHOICES
from apps.core.models import TimestampModel


GALLERY_TYPE = (
    ("CLIENT_GALLERY", "CLIENT GALLERY"),
    ("BRIDAL_SERVICE_GALLERY", "BRIDAL SERVICE GALLERY"),
)


class Gallery(TimestampModel):
    gallery_type = models.CharField(max_length=100, choices=GALLERY_TYPE, blank=True, null=True,
                                    help_text="The gallery depends on type")
    name = models.CharField(max_length=100, unique=True, blank=True, null=True, help_text="The name")
    description = models.TextField(max_length=1000, blank=True, null=True, help_text="The description of the Item")
    featured_image =  models.ImageField(upload_to='Gallery/pics', help_text="Background Image", blank=True, null=True)
    mobile_image =  models.ImageField(upload_to='Gallery/mobile_images', blank=True, null=True,
                                       help_text="Upload Image for Mobile")
    desktop_image =  models.ImageField(upload_to='Gallery/desktop_images', blank=True, null=True,
                                        help_text="Upload Image for Desktop")
    icon_image =  models.ImageField(upload_to="Gallery/icon-images", blank=True, null=True,
                                     help_text="Gallery Icon Image")
    hosted_video = models.FileField(upload_to='Gallery/videos', max_length=200, null=True, blank=True,
                                    help_text="Video upload file")
    provider = models.CharField(max_length=100, choices=VIDEO_PROVIDER_CHOICES, null=True, blank=True,
                                help_text="Video provider name")
    provider_url = models.URLField(max_length=300, null=True, blank=True, help_text="Video URL")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Galleries'
        ordering = ("-id",)

    def __str__(self):
        return self.name if self.name is not None else str(self.id)




class GalleryItem(TimestampModel):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="gallery_items")
    mobile_image =  models.ImageField(upload_to='Gallery/mobile_images', blank=True, null=True,
                                       help_text="Mobile Image for hover image or carousel image")
    desktop_image =  models.ImageField(upload_to='Gallery/desktop_images', blank=True, null=True,
                                        help_text="Desktop Image for hover image or carousel image")
    hosted_video = models.FileField(upload_to='Gallery/videos', max_length=200, null=True, blank=True,
                                    help_text="Video upload file")
    provider = models.CharField(max_length=100, choices=VIDEO_PROVIDER_CHOICES, null=True, blank=True,
                                help_text="Video provider name")
    provider_url = models.URLField(max_length=300, null=True, blank=True, help_text="Video URL")

    class Meta:
        verbose_name_plural = 'Gallery Items'
        ordering = ("-id",)

    def __str__(self):
        return self.gallery.name if self.gallery.name is not None else str(self.id)
