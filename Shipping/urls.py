from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Ship/', include('Ship.api.urls', namespace='ship')),
    path('api/Product/', include('Product.api.urls')),
    path('api/Port/', include('Port.api.urls')),
    path('api/account/', include('account.api.urls')),

]
