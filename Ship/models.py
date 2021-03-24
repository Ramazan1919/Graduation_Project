import random
import uuid

from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.text import slugify

from Port.models import Port
from Product.models import Product
from Shipping import settings


class Ship(models.Model):
    class ShipType(models.TextChoices):
        Plane = 'Uçak',
        Truck = 'Kamyon',
        Ship = 'Gemi',

    Ship_Type = models.CharField(
        max_length=10,
        choices=ShipType.choices,
        default=ShipType.Truck,
    )

    class LocationsType(models.TextChoices):
        Mersin = 'Mersin',
        Istanbul = 'Istanbul',

    Locations_Type = models.CharField(
        max_length=10,
        choices=LocationsType.choices,
        default=LocationsType.Mersin,
    )
    title = models.CharField(max_length=100)
    Active = models.BooleanField(default=False)
    TrackingId = models.CharField(max_length=40, default=uuid.uuid4, editable=False)
    SippingContent = models.TextField(max_length=100)
    SippingContent = models.CharField(max_length=100)
    ShippingNotes = models.TextField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150, editable=False)

    # Tarihler düzenlenecek

    ArrivingDate = models.DateTimeField()
    DepartureDate = models.DateTimeField(auto_now_add=True, editable=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    Products = models.ForeignKey(Product, related_name='ship_set', on_delete=models.CASCADE, null=False)

    Ports = models.ForeignKey(Port, related_name='ship_set', on_delete=models.CASCADE, null=False)

    # her olıuşturulan ship için farklı bir isim dönmeyi sağlar
    def __str__(self):
        return self.title

    # Slug için
    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique = slug
        number = 1
        while Ship.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug, number)
            number += 1

        return unique

    # Her bir Ship oluşturulduğunda başta id yok daha sonraki dit ve düzenlemelerde var ama
    # bu işlemleri otomatikleştirmek için
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
            self.modified = timezone.now()
            self.slug = self.get_slug()
            return super(Ship, self).save(*args, **kwargs)


