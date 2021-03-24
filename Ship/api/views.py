from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView

from Product.models import Product
from Ship.api.pagination import ShipPagination
from Ship.api.permissions import IsOwner
from Ship.api.serializers import ShipSerializers, ShipCreateSerializers
from Ship.models import Ship

from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated
)


class ShipAPIView(ListAPIView):
    serializer_class = ShipSerializers
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    pagination_class = ShipPagination

    # Queryset üstünden filtreleme işlemleri yapabiliyoruz

    def get_queryset(self):
        queryset = Ship.objects.filter(Active=True)
        return queryset

    # Filtreleme işlemleri için
    # def get_queryset(self):


class ShipDetailAPIView(RetrieveAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializers
    lookup_field = 'pk'


class ShipDeleteAPIView(DestroyAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializers
    lookup_field = 'pk'
    permission_classes = [IsOwner]


class ShipUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializers
    lookup_field = 'pk'
    permission_classes = [IsOwner]


class ShipCreateAPIView(CreateAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipCreateSerializers
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self, obj):
        user = self.request.user
        #product=self.Product.objects.fiter(Product.hasShip=False)
        #product = self.filter_queryset(queryset=Product.hasShip == False)
        return self.queryset.filter(owner=user )
