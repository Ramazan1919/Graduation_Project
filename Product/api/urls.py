from django.urls import path, include

from Product.api.views import ProductAPIView, ProductDetailAPIView,ProductCreateAPIView,ProductUpdateAPIView
app_name = "product"
urlpatterns = [

    path('List', ProductAPIView.as_view(), name='List'),
    path('detail/<pk>', ProductDetailAPIView.as_view(), name='detail'),
    path('create', ProductCreateAPIView.as_view(), name='create'),
    path('update/<pk>', ProductUpdateAPIView.as_view(), name='update'),
]
