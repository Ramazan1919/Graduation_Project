from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from Product.api.pagination import ProductPagination
from Product.api.permission import IsOwner
from Product.api.serializers import ProductSerializers, ProductCreateSerializers
from Product.models import Product


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = ProductPagination

    def get_queryset(self):

        return self.queryset.filter(hasShip=False)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'


class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    permission_classes = [IsOwner]


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(owner=user)







