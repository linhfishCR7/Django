from rest_framework import serializers
from cities_app.models import City

class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    active = serializers.BooleanField()

    def create(self,validated_data):
        return City.objects.create(**validated_data)

    def update(self,instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance