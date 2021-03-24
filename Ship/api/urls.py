from django.urls import path, include

from Ship.api.views import ShipAPIView, ShipDetailAPIView, ShipUpdateAPIView, ShipDeleteAPIView, ShipCreateAPIView

app_name = "ship"
urlpatterns = [

    path('list', ShipAPIView.as_view(), name='list'),
    path('detail/<pk>', ShipDetailAPIView.as_view(), name='detail'),
    path('update/<pk>', ShipUpdateAPIView.as_view(), name='update'),
    path('delete/<pk>', ShipDeleteAPIView.as_view(), name='delete'),
    path('create/', ShipCreateAPIView.as_view(), name='create'),
]
