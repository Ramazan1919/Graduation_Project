from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Ship.models import Ship


class ShipSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ship:detail',
        lookup_field='pk'
    )
    username = serializers.SerializerMethodField(method_name='username_new')
    products = serializers.SerializerMethodField(method_name='product_new')
    ports = serializers.SerializerMethodField(method_name='port_new')

    class Meta:
        model = Ship
        fields = '__all__'

    def username_new(self, obj):
        return str(obj.owner.username)

    def product_new(self, obj):
        return str(obj.Products.ProductName)

    def port_new(self, obj):
        return str(obj.Ports.name)


class ShipCreateSerializers(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(method_name='product_new')

    ports = serializers.SerializerMethodField(method_name='port_new')

    class Meta:
        model = Ship
        fields = '__all__'

    # exclude = 'TrackingId'

    def product_new(self, obj):
        return str(obj.Products.ProductName)

    def port_new(self, obj):
        return str(obj.Ports.name)
