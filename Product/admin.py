from django.contrib import admin

# Register your models here.
from Product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['hasShip', 'ProductName']

    class Meta:
        model = Product


admin.site.register(Product,ProductAdmin)
