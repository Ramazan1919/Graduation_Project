from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from Shipping import settings


class Port(models.Model):
    class PortType(models.TextChoices):
        Liman = 'Liman',
        Sehir = 'Sehir',
        Okyanus = 'Okyanus',

    Port_Type = models.CharField(
        max_length=10,
        choices=PortType.choices,
        default=PortType.Liman,
    )
    name = models.CharField(max_length=25)
    Continent = models.CharField(max_length=25)
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



    def __str__(self):
        return self.name

    # Slug için
    def get_slug(self):
        slug = slugify(self.name.replace("ı", "i"))
        unique = slug
        number = 1
        while Port.objects.filter(slug=unique).exists():
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
            return super(Port, self).save(*args, **kwargs)


