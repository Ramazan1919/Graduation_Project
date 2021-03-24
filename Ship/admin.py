from django.contrib import admin

# Register your models here.
from Ship.models import Ship


# admin panel özelleştirmeleri için
class ShipAdmin(admin.ModelAdmin):
    list_display = ['title', 'DepartureDate', 'slug']
    list_display_links = ['title', 'DepartureDate']
    search_fields = ['title', 'TrackingId']

    class Meta:
        model = Ship


admin.site.register(Ship, ShipAdmin)
