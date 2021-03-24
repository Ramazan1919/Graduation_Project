from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from Port.api.pagination import PortPagination
from Port.api.permissions import IsOwner
from Port.api.serializers import PortSerializers
from Port.models import Port


class PortAPIView(ListAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializers
    pagination_class =PortPagination


class PortDetailAPIView(RetrieveAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializers
    lookup_field = 'pk'

class PortCreateAPIView(CreateAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializers
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)