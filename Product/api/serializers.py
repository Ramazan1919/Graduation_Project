from rest_framework import serializers

from Product.models import Product


class ProductSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:detail',
        lookup_field='pk'
    )

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
