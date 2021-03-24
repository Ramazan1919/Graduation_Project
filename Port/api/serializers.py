from rest_framework import serializers

from Port.models import Port


class PortSerializers(serializers.ModelSerializer):
    users = serializers.SerializerMethodField(method_name='users_new')
    class Meta:
        model = Port
        fields = '__all__'

    def users_new(self, obj):
            return str(obj.owner.username)
