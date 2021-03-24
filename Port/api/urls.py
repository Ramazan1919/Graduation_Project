from django.urls import path, include

from Port.api.views import PortAPIView, PortDetailAPIView, PortCreateAPIView

urlpatterns = [

    path('list', PortAPIView.as_view(), name='list'),
    path('detail/<pk>', PortDetailAPIView.as_view(), name='detail'),
    path('create/', PortCreateAPIView.as_view(), name='create'),
]