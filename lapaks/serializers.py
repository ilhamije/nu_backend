from rest_framework import serializers

from .models import Lapak


class LapakSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lapak
        fields = '__all__'

    def create(self, validated_data):
        return Lapak.objects.create(**validated_data)

    def to_representation(self, instance: Lapak):
        data = dict()
        data['title'] = instance.title
        data['description'] = instance.description
        data['picture1'] = instance.picture1
        data['picture2'] = instance.picture2
        data['picture3'] = instance.picture3
        data['city'] = instance.city
        data['address'] = instance.address
        data['related_url'] = instance.related_url
        data['latitude'] = instance.latitude
        data['longitude'] = instance.longitude
        data['additional_info'] = instance.additional_info
        data['created_at'] = instance.created_at
        data['updated_at'] = instance.updated_at
        # data['user'] = instance.user_id

        return data
