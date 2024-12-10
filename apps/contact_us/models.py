from django.core.exceptions import ValidationError
from django.db import models
from apps.carousel.models import Carousel
from apps.core.models import TimestampModel
from apps.service.models import Service

ENQUIRY_TYPE_CHOICES = (
    ("GENERAL_ENQUIRY", "GENERAL ENQUIRY"),
    ("OVERALL_PACKAGE", "OVERALL PACKAGE"),
    ("BRAND_PARTNERS", "BRAND PARTNERS"),
    ("OTHERS", "OTHERS"),
)


class Address(TimestampModel):
    """
    A model representing an address
    """
    address_line1 = models.CharField(max_length=200, blank=True, null=True)
    address_line2 = models.CharField(max_length=200, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True, help_text="Nearby landmark")
    city = models.CharField(max_length=50, blank=True, null=True, help_text="City Name")
    state = models.CharField(max_length=50, blank=True, null=True, help_text="State Name")
    country = models.CharField(max_length=50, blank=True, null=True, help_text="Country Name")
    pincode = models.PositiveIntegerField(blank=True, null=True, help_text="Address Pincode")
    mobile = models.TextField(blank=True, null=True, help_text="Comma-separated mobile numbers")
    email = models.TextField(blank=True, null=True, help_text="Comma-separated email addresses")
    is_active = models.BooleanField(default=True, help_text="Status")
    is_default = models.BooleanField(default=False, help_text="Default Address")
    full_address = models.TextField(max_length=1000, blank=True, null=True, help_text="Full Address")

    class Meta:
        verbose_name_plural = "Addresses"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.id} - {self.city or 'No City'} - {self.state or 'No State'} - {self.pincode or 'No Pincode'}"

    def clean(self):
        """
        Custom validation to ensure either `full_address` or `address_line1` is provided.
        """
        if self.full_address and (self.address_line1 or self.address_line2):
            raise ValidationError(
                "Please provide either a full address or address lines, not both."
            )





class ContactEnquiry(TimestampModel):
    """
    To save the Contact us enquiries Django model
    """
    first_name = models.CharField(max_length=40, help_text="Enquiry person's first name")
    last_name = models.CharField(max_length=40, help_text="Enquiry person's last name")
    email = models.EmailField(max_length=255, help_text="Enquiry person's email")
    phone_number = models.CharField(max_length=10, help_text="Enquiry person's mobile number")
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True,
                                help_text="The service enquiring about")
    artist = models.ForeignKey(Carousel, on_delete=models.SET_NULL, blank=True, null=True,
                               help_text="The service enquiring about")
    message = models.TextField(max_length=1000, blank=True, null=True, help_text="The Enquiry Message")
    enquiry_type = models.CharField(max_length=50, choices=ENQUIRY_TYPE_CHOICES, help_text="The Enquiry Type")

    class Meta:
        verbose_name_plural = 'Enquiries (Contact Us)'

    def __str__(self):
        return self.first_name
