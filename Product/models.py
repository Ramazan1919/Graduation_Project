from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.text import slugify

from Shipping import settings


class Product(models.Model):
    class CategoryType(models.TextChoices):
        Doc = 'Doc',
        Steel = 'Steel',
        Box = 'Box',

    Category_Type = models.CharField(
        max_length=12,
        choices=CategoryType.choices,
        default=CategoryType.Box,
    )

    ProductName = models.CharField(max_length=25)
    CreatingDate = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    hasShip = models.BooleanField(default=False)

    owner 	= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.ProductName

    # Slug için
    def get_slug(self):
        slug = slugify(self.ProductName.replace("ı", "i"))
        unique = slug
        number = 1
        while Product.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug, number)
            number += 1

        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
            self.modified = timezone.now()
            self.slug = self.get_slug()
            return super(Product, self).save(*args, **kwargs)
